import math
import sys


#Global Variable tracking the final indivisible value
last_indivisible = None

#Global Variable of type list tracking all values found to be indivisible and 
#all values found to be divisible in order to speed up program and not 
#recalculate values already calculated
undivis_list = list()
divis_list = list()

#Global Variable of type list tracking all values already calculated in order
#to prevent duplicate calculations
values_seen = list()

#Global Variable tracking all denominations
CURR_DENOM = [538, 19]
#CURR_DENOM = [538, 101, 19]

#Global Variables for tracking circular buffer meant to exit program once 19
#consecutive divisible values are detected as that signifies no more indivisible
#values will occur
circular_buffer = [False] * min(CURR_DENOM)
circular_buffer_index = 0

#Global Constants specifying range of values to calculate
START_VAL = 0
END_VAL = 100000


def circular_buff(value):
    global CURR_DENOM

    global circular_buffer
    global circular_buffer_index
    global last_indivisible

    circular_buffer[circular_buffer_index] = value

    circular_buffer_index += 1
    circular_buffer_index = circular_buffer_index % min(CURR_DENOM)

    #If there are no occurences of False in the circular buffer the last 19
    #values were divisible meaning all following values will be divisible
    #so we should exit program and print final indivisible value
    if False not in circular_buffer:
        print "We have had 19 consecutive divisible values, all other values will be divisible"
        print "Highest value indivisible by denominations: {0} is {1}".format(CURR_DENOM, last_indivisible)
        exit(1)


def evenly_divis(value):
    global CURR_DENOM

    global values_seen
    global undivis_list
    global divis_list

    outcome_list = list()


    #For each denomination of currency in this scenario
    for denom in CURR_DENOM:

        #Subtract that denomination from the value
        remain = value - denom

        #If the remainder is 0, the value is evenly divisible, return True
        if remain == 0:
            return True

        #If the remainder is a value known to be divisible return True
        elif remain in divis_list:
            return True

        #If the remainder is greater than 0 but smaller than our smallest
        #denomination, the value is indivisible.  Mark this permutation as False
        elif remain > 0 and remain < min(CURR_DENOM):
            outcome_list.append(False)

        #If the remainder is a value known to be indivisible, mark this
        #permutation as False
        elif remain in undivis_list:
            outcome_list.append(False)

        #If the remainder is not known to be indivisible, recursively call
        #function on the remainder
        elif remain > 0:

            #If we have already calculated this value before, do not recalculate
            if remain in values_seen:
                outcome_list.append(False)

            #If we have not calculated this value, calculate and add to list
            #of calculated values
            else:
                outcome_list.append(evenly_divis(remain))
                values_seen.append(remain)

    #If any of the recursive calls have returned True, signifying divisibilty
    #return True
    if True in outcome_list:
        return True

    #If no recursive call has returned True, the value is indivisible return
    #False
    else:
        return False


def main():
    global START_VAL
    global END_VAL

    global values_seen
    global undivis_list
    global divis_list
    global last_indivisible

    #Calculate divisibily for each value in the specified range
    for i in range(START_VAL, END_VAL):
        
        #Clear values seen list as it must be empty for each value calculated
        values_seen = []

        outcome = evenly_divis(i)

        if outcome == False:
            undivis_list.append(i)
            last_indivisible = i

        else:
            divis_list.append(i)
    
        print "{0}, {1}".format(i, str(outcome))
        circular_buff(outcome)


main()
