import math
import random

'''
all_nums = list()
for i in range(10000000):
    num = (format(i, '07d'))
    all_nums.append([num.count('0'), num.count('1'), num.count('2'), num.count('3'), num.count('4'), num.count('5'), num.count('6'), num.count('7'), num.count('8'), num.count('9')])


def num_overlap(n):
    global all_nums
    count = -1

    for i in range(10000000):
        if all_nums[i] == all_nums[n]:
                count += 1

    return count


def main():
    global all_nums
    count = 0

    for i in range(10000000):
        runCount = num_overlap(i)
        i = format(i, '07d')
        print "Phone Number: {0} has {1} overlaps".format(i, runCount)
        count += runCount

    print "Overall Statistics: {0}% Chance of Overlap".format(count / (10000000 * 9999999.0))

main()
'''











numbers = list()
for i in range(10000000):
    iForm = format(i, '07d')
    numbers.append([iForm, [iForm.count('0'), iForm.count('1'), iForm.count('2'), iForm.count('3'), iForm.count('4'), iForm.count('5'), iForm.count('6'), iForm.count('7'), iForm.count('8'), iForm.count('9')]])




def num_overlap(n):
    global numbers
    count = 0

    marked_for_removal = list()

    for elem in numbers:
        if n[1] == elem[1]:
            marked_for_removal.append(elem)
            count += 1

    for num in marked_for_removal:
        numbers.remove(num)

    '''for i in range(100):
        print numbers[i]'''

    return count



def main():
    global numbers
    count_list = list()



    while len(numbers) != 0:
        print numbers[0][0]
        count = num_overlap(numbers[0])
        count_list.append(count)
        print "last count: {0}, remaining numbers: {1}".format(count, len(numbers))

    print count_list


main()



def debug_main():

    for i in range(100):
        print numbers[i]

debug_main()



















