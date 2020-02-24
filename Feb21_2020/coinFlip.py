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
THRESH_DEBUG = True

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
#   scenarios when value is > thresh use coin 1
#   scenarios when value is < thresh use coin 2
threshold = -0.5


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
        node_heads[PROB] = node_heads[PROB] * .5
        if threshold > node_heads[VAL]:
            node_heads[STEP] = HIGHVAR
        else:
            node_heads[STEP] = LOWVAR

        node_tails = list(node)
        node_tails[VAL] = node_tails[VAL] - node_tails[STEP]
        node_tails[PROB] = node_tails[PROB] * .5
        if threshold > node_tails[VAL]:
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
    global threshold

    if 0 > threshold:
        root_node = [0, 1, LOWVAR]
    else:
        root_node = [0, 1, HIGHVAR]
    curr_level = list()
    curr_level.append(root_node)

    next_level = list()

    curr_flip = 0


def init_thresholds(thresh):
    global threshold

    threshold = thresh


def run_for_threshold():
    global curr_flip

    init_level()

    while curr_flip < 100:

        if DEBUG == True:
            print curr_level
            print "Coin Flip {0}".format(curr_flip)

        calc_next_level()

    probability = calc_prob_win()
    print "Probability: {0}".format(probability)
    if THRESH_DEBUG:
        print threshold
    return probability


for i in range(-10,10):

    init_thresholds(i+.5)
    run_for_threshold()
