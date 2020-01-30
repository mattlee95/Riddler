# p(1try) + p(2try) = 1
# p(1defend)_+ p(2defend) = 1

# 2 try and 2 defedned = p(2try) * p(2defend) * (.4 * 2)
# 2 try and 1 defended = p(2try) * p(1defend) * (.6 * 2)

# 1 try and 2 defended = p(1try) * p(2defend) * (1 * 1)
# 1 try and 1 defended = p(1try) * p(1defend) * (.9 * 1)


RESOLUTION = 1000



def find_opponent_optimal_strategy(p1try):

    minPPT = 2
    minPPTstrat = None

    for p1def in range(RESOLUTION+1):

        p1def /= float(RESOLUTION)

        # 2 try 2 defend
        expected = (1-p1try) * (1-p1def) * (.4 * 2)
        # 2 try 1 defend
        expected += (1-p1try) * (p1def) * (.6 * 2)
        # 1 try 2 defend
        expected += (p1try) * (1-p1def) * (1 * 1)
        # 1 try 1 defend
        expected += (p1try) * (p1def) * (.9 * 1)

        #print "expected: {0}, p(1def): {1}".format(expected, p1def)

        if expected < minPPT:
            minPPT = expected
            minPPTstrat = p1def

    return minPPT, minPPTstrat


def find_team_optimal_strategy():

    maxPPT = 0
    maxPPTstrat = None
    maxPPToppStrat = None

    p1trylst = list()
    expectedlst = list()

    for p1try in range(RESOLUTION):

        p1try /= float(RESOLUTION)

        expected, oppStrat = find_opponent_optimal_strategy(p1try)

        if expected > maxPPT:
            maxPPT = expected
            maxPPTstrat = p1try
            maxPPToppStrat = oppStrat

        p1trylst.append(p1try)
        expectedlst.append(expected)
        #print "{0}, {1}".format(p1try, expected)

    print "Completed Optimation"
    print "Optimized PPT: {0}, Optimized P(1try): {1}, Opponent Optimal Response: {2}".format(maxPPT, maxPPTstrat, maxPPToppStrat)

    return p1trylst, expectedlst


import matplotlib.pyplot as plt


probabilities, expectedValues = find_team_optimal_strategy()

plt.scatter(probabilities, expectedValues, s=5, c='black')
plt.title('Scatter Plot of Extra Point Try Probabilities and Expected Points Per Try')
plt.xlabel('Probability of Going for 1 Point Try')
plt.ylabel('Expected Points Per Try Given Optimal Opponent Strategy')

plt.show()
