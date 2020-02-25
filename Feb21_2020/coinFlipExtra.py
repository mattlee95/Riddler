'''
from itertools import product
PERMS = list(product([1,-1],repeat = 100))
print len(PERMS)
'''

'''
So, since there is no way running through all permutations is going to work
on this banged up iMac, I think I'm going to privot my solution methodology
to calculate how cases permutate out from the beginning mode and track
probabilities.  I'm thinking of using this struct:

Node : [int val, float probability, int step]

After every turn we split every node into 2 new nodes:

NodeHeads : [int val + step, float probability * .5, int step]
NodeTails : [int val - step, float probability * .5, int step]

We can combines nodes at every level by adding the probabilities of nodes
with the same val and step.
'''
#Debugging Globals
DEBUG = False
THRESH_DEBUG = False

#Index Globals
VAL = 0
PROB = 1
STEP = 2

#Variance Globals
LOWVAR = 1
HIGHVAR = 2

#Permuation Tree
curr_level = None
next_level = None
curr_flip = None

#Thresholds to swap variance strategies (coins)
threshold = None

#Probability of 1 point coin
p_heads = None


def calc_prob_win():
    global curr_level

    prob_win = 0

    for node in curr_level:

        if node[VAL] > 0:
            prob_win += node[PROB]

    return prob_win


def calc_next_level():
    global curr_level
    global next_level
    global curr_flip
    global threshold

    flag_incorperated_h = None
    flag_incorperated_t = None

    next_level = list()

    for node in curr_level:

        flag_incorperated_h = False
        flag_incorperated_t = False

        node_heads = list(node)
        node_heads[VAL] = node_heads[VAL] + node_heads[STEP]
        if node_heads[STEP] == HIGHVAR:
            node_heads[PROB] = node_heads[PROB] * .5
        else:
            node_heads[PROB] = node_heads[PROB] * p_heads
        if threshold[curr_flip] > node_heads[VAL]:
            node_heads[STEP] = HIGHVAR
        else:
            node_heads[STEP] = LOWVAR

        node_tails = list(node)
        node_tails[VAL] = node_tails[VAL] - node_tails[STEP]
        if node_tails[STEP] == HIGHVAR:
            node_tails[PROB] = node_tails[PROB] * .5
        else:
            node_tails[PROB] = node_tails[PROB] * (1 - p_heads)
        if threshold[curr_flip] > node_tails[VAL]:
            node_tails[STEP] = HIGHVAR
        else:
            node_tails[STEP] = LOWVAR


        for i in range(len(next_level)):

            if ((flag_incorperated_h == False) and (next_level[i][VAL] == node_heads[VAL]) and (next_level[i][STEP] == node_heads[STEP])):
                next_level[i][PROB] = next_level[i][PROB] + node_heads[PROB]
                flag_incorperated_h = True

            if ((flag_incorperated_t == False) and (next_level[i][VAL] == node_tails[VAL]) and (next_level[i][STEP] == node_tails[STEP])):
                next_level[i][PROB] = next_level[i][PROB] + node_tails[PROB]
                flag_incorperated_t = True

        if flag_incorperated_h == False:
            next_level.append(node_heads)

        if flag_incorperated_t == False:
            next_level.append(node_tails)


    curr_flip += 1
    curr_level = next_level
    next_level = list()

def init_level():
    global curr_level
    global next_level
    global curr_flip

    if 0 < threshold[0]:
        root_node = [0, 1, HIGHVAR]
    else:
        root_node = [0, 1, LOWVAR]
    curr_level = list()
    curr_level.append(root_node)

    next_level = list()

    curr_flip = 0


def init_thresholds(thresh):
    global threshold

    threshold = [thresh] * 100


def run_for_threshold():
    global curr_flip

    init_level()

    while curr_flip < 100:

        if DEBUG == True:
            print curr_level
            print "Coin Flip {0}".format(curr_flip)

        calc_next_level()

    probability = calc_prob_win()
    #print "Probability: {0}".format(probability)
    if THRESH_DEBUG:
        print threshold
    return probability

#init_thresholds(0,0)
#run_for_threshold()

'''
Down here is the fun stuff, now we try to optimize the threshold levels by turn
to get the highest expected win rate.

So the high level methodology behind the optimazation is to start the thresholds
with all the same value for every turn, at a higher value than I think would
be optimal

Then I will begin to subract one from the nth array and check if that imporved the
chances.  I will continue to subract from the n-1th array until it no longer optimizes

I will then loop back to the nth array and subract again and complete the cycle until
I can no longer optimize the solution by bringing the threshold lower.

This in theory should result in a completely optimzed threshold for this problem

Turns out the most optimal thresholds are 0, the answer is as simple as:
 - If your current score is positive roll the 1 pointer
 - If your current score is negative roll the 2 pointer
'''


def optimize_threshold_old(coin_prob):
    global threshold
    global p_heads

    p_heads = coin_prob
    print p_heads

    limit = 0

    init_thresholds(limit)

    last_last_prob = 0
    last_prob = 0
    prob = 0

    for i in range(100):

            creep_thresh(i)

            prob = run_for_threshold()

            #if prob <= last_prob and prob <= last_last_prob:
               #break

            last_last_prob = last_prob
            last_prob = prob

    optimized_prob = run_for_threshold()

    print "1-Point Coin Heads Probability: {0}".format(coin_prob)
    print "Optimzed Probability: {0}".format(optimized_prob)
    print "High Var to Low Var Thresh: {0}".format(threshold)

def creep_thresh(i):
    global threshold
    '''
    returns 1 if function futher optimized
    returns 0 if function could not futher optimize
    '''
    best_prob = run_for_threshold()
    best_thresh = list(threshold)
    prob = 0

    for n in range(min(2 * (i + 1) + 1,101-i)):
        threshold[i] = threshold[i] + 1
        prob = run_for_threshold()

        if prob >= best_prob:
            best_prob = prob
            best_thresh = list(threshold)

        print prob
        print threshold

    threshold = list(best_thresh)
    print "Best Probability: {0}".format(run_for_threshold())

optimize_threshold_old(0.05)

'''
def optimize_unfair_coin():

    for i in range(0,10):
        optimize_threshold_old(.5 - (i*.05))


optimize_unfair_coin()
'''
