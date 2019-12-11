'''
Equation of average number of moves given threshold strategy

threshold = maximum distance to use next over random
n = song population size
x = number of random uses

SUM(x:0, Inf)   ((threshold+1) / n) * ((n - (threshold+1) / n) ^^ x * ((threshold / 2) + x)

                      ^                   ^                            ^
                      |                   |                            |
                      |                   |                            |
                      |                   |        Statement for the average expected moves for case
                      |                   |
                      |        Statement for the probability that random falls outside thresh
                      |
 Statement for the probability that random falls inside thresh

'''


# Will not calculate the sum to infinity, this represents the upper limit of our summation
CUTOFF = 100 * 100


def calc_equation(x, n, thresh):

    ret = (float(thresh+1) / n) * ((float(thresh) / 2)  + x) * pow(((float(n) - (thresh+1)) / n), x)

    return ret


def calc_sumation(n, thresh):

    global CUTOFF

    total = 0

    for x in range(CUTOFF):
        total += calc_equation(x, n, thresh)

    return tot


def main(n):

    print ""

    for thresh in range(0,100):
        outcome = calc_sumation(n, thresh)

        #print "For n = {0}, Threshold = {1}: Expected Moves = {2}".format(n, thresh, outcome)
        print "{0}, {1}".format(thresh, outcome)

        last_outcome = outcome

main(100)
