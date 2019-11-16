
'''
THRESHOLD_PROB is the programs protections from calculating infintely for incredibly
unlikely scenarios like repeating 1's (i.e. 0.11111....)

If the probability of a specific scenario dips below this threshold the program will
end that scenario and calculate the expected value of that path
'''
THRESHOLD_PROB = 0.00000001

'''
Tracking the sum of all expected outcomes
'''
current_average = 0

'''
Structure of node in tree
[int current_value, int divisor (starts at 10), float prob]
'''
IND_VAL = 0
IND_DIV = 1
IND_PROB = 2

'''
Idea here is that we are solving a tree where we dont care about the connections between
levels only the contents of each level of the tree
'''
next_level = []
current_level = []


def init():
    global current_level
    global next_level
    global current_average

    # Setting all of the globals to be the default values to initialize

    current_average = 0
    next_level = []
    current_level = [[.1, 100, .1], [.2, 100, .1], [.3, 100, .1], [.4, 100, .1], [.5, 100, .1], [.6, 100, .1], [.7, 100, .1], [.8, 100, .1], [.9, 100, .1]]

def add_node_to_next_level(node):
    global next_level

    # Checks to see if a node representing this scpecific value already exists in
    # the next level.  If so we add the probability of this node to the matching
    # node.  If not append this node to the list tracking the next level

    for existing_node in next_level:
        if existing_node[IND_VAL] == node[IND_VAL]:
            existing_node[IND_PROB] = existing_node[IND_PROB] + node[IND_PROB]
            return

    next_level.append(node)

def solve_node(node):
    global THRESHOLD_PROB
    global current_average

    # If the probability of this scenario falls under our probability threshold
    # do not permutate further, get an estimated value for this path now
    if node[IND_PROB] <= THRESHOLD_PROB:
        current_average += node[IND_VAL] * node[IND_PROB]
        return

    # Variable to track the value of the last number to be added to the value
    last_val = int(str(node[IND_VAL])[len(str(node[IND_VAL]))-1])
    # Variable tracking the probability that this value will not change after
    # rolling the dice
    prob_unchanged = 0

    # Iterate through every possible roll
    for i in range(10):

        # If the value is greater than the final addition, the value will not change
        if i > last_val:
            prob_unchanged += .1

        # If the value is less than the final addition and not zero, add the value
        # to the end of the value and add it to the next level
        elif i != 0:
            new_node = list(node)
            new_node[IND_VAL] = new_node[IND_VAL] + (float(i) / new_node[IND_DIV])
            new_node[IND_DIV] = new_node[IND_DIV] * 10
            new_node[IND_PROB] = new_node[IND_PROB] * .1
            add_node_to_next_level(new_node)

        # If the dice rolls zero, this scenario is over add the expected value to the
        # global tracking the running sum
        else:
            current_average += node[IND_VAL] * node[IND_PROB] * 0.1

    # Add unchanged node to next level
    unchanged_node = list(node)
    unchanged_node[IND_PROB] = unchanged_node[IND_PROB] * prob_unchanged
    add_node_to_next_level(unchanged_node)


def solve_level():
    global current_level
    global next_level

    # Iterate through every node in the current level and solve for the scenario
    for node in current_level:
        solve_node(node)

    # Switch the current_level with the holder variable next_level
    current_level = next_level
    next_level = []


def main(thresh):
    global current_level
    global THRESHOLD_PROB

    THRESHOLD_PROB = thresh

    init()
    while len(current_level) != 0:
        solve_level()

    print "average: {0} with a threshold prob of {1}".format(current_average, THRESHOLD_PROB)

main(.1)
main(.01)
main(.001)
main(.0001)
main(.00001)
main(.000001)
main(.0000001)
main(.00000001)
main(.000000001)
main(.0000000001)
main(.00000000001)
main(.000000000001)
main(.0000000000001)
main(.00000000000001)
