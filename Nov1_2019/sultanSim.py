import math
import random

from itertools import permutations


# THRESHOLD is a list of int type variables meant to represent the mininum standing
# of the suiter at that index compared to those rejected in order to be selected
THRESHOLD = [0, 0, 0, 0, 0, 0, 0, 0]

# REJECT_UNTIL represents the amount of suiters who should be automatically rejected
# during the process.
REJECT_UNTIL = 4

# PERMS is a list of lists representing all possible permutations of 1 through 10
PERMS = list(permutations(range(1,11)))


def reset_threshold():
    global THRESHOLD

    # Reset THRESHOLD to begin optimization from known point
    THRESHOLD = [0, 0, 0, 0, 0, 0, 0, 0]


def choose_suiter(randomized_tup):
    global THRESHOLD
    global REJECT_UNTIL

    # Change tuple arguement to list
    randomized_list = list(randomized_tup)

    # Starting at the first index that shouldn't be automatically rejected to the final
    # index in the list
    for i in range(REJECT_UNTIL, 9):

        # Create holder list of all previous elements before one being evaluated in order
        # to construct sorted list of all previously rejected candidates
        holder = randomized_list[:i]
        holder.sort()

        # If the evaulated index scores higher than the threshold index in the sorted list
        # of previously rejected candidates selected the evauluated candidate
        if randomized_list[i] < holder[THRESHOLD[i-1]]:
            return randomized_list[i]

    # If we get to this point all 9 other candidates have been rejected.  We must select
    # the final candidate
    return randomized_list[9]


def main():
    global RUNS
    global PERMS

    # total_sum represents the sum of each suiters ranking in order to calculate average
    # score for threshold values in set of all possible permutations
    total_sum = 0

    # For every permutation in the permutation set
    for suiters in PERMS:

        # Use given threshold to choose a suiter and save the ranking. Add the ranking
        # to the sum we are using to track results
        outcome = choose_suiter(suiters)
        total_sum += outcome

    # Print and return final stats for threshold efficacy
    print "Final Stats: {0} Average Suiter Positon".format(float(total_sum)/float(len(PERMS)))
    return (float(total_sum)/float(len(PERMS)))


def optimize(reject_index):
    global THRESHOLD
    global REJECT_UNTIL

    print "Running optimization for dowry problem: with auto-rejection until index {0}".format(reject_index)

    # Set the REJECT_UNTIL value equal to the reject_index arguement.  Reset the
    # THRESHOLD for new optimization
    REJECT_UNTIL = reject_index
    reset_threshold()

    # For all elements in THREHSOLD following the REJECT_UNTIL index run the following
    # optimization loop
    for i in range(REJECT_UNTIL, len(THRESHOLD)):

        # Flag tracking if index has been optimized in the incremental run
        flag_index_optimized = False

        while (flag_index_optimized != True):

            # Increment index's threshold value by 1 and comapre to previous outcome.
            preopt_val = main()
            THRESHOLD[i] = THRESHOLD[i] + 1
            postopt_val = main()

            # If new outcome is less optimized than previous value move back to more
            # optimized threshold value and set optimized flag to True to exit loop
            if preopt_val < postopt_val:
                THRESHOLD[i] = THRESHOLD[i] - 1
                flag_index_optimized = True

        print str(THRESHOLD) + " Auto-Rejecting Until Index: " + str(REJECT_UNTIL)

    # For all elements in THRESHOLD following the REJECT UNTIL index in reverse order
    # run the following optimization loop
    for n in range(len(THRESHOLD)-1, REJECT_UNTIL-1, -1):

        # Flag tracking if index has been optimized in the decremental run
        flag_index_optimized = False

        while (flag_index_optimized != True and THRESHOLD[n] >= 1):

            # Decrement index's threshold value by 1 and comapre to previous outcome.
            preopt_val = main()
            THRESHOLD[n] = THRESHOLD[n] - 1
            postopt_val = main()

            # If new outcome is less optimized than previous value move back to more
            # optimized threshold value and set optimized flag to True to exit loop
            if preopt_val < postopt_val:
                THRESHOLD[n] = THRESHOLD[n] + 1
                flag_index_optimized = True

        print str(THRESHOLD) + " Auto-Rejecting Until Index: " + str(REJECT_UNTIL)


# Run the optimization function for all legal index to auto reject until
for i in range(1,8):
    optimize(i)
