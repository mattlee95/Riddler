import random
import os

'''

Script for simulating the problem using the Python random library

'''


threshold_next = 10
RUNS = 100 * 100 * 100


def simOneRun():

    global threshold_next

    num_moves = 0
    distance = random.randint(0, 99)

    while (distance > threshold_next):

        distance = random.randint(0, 99)
        num_moves += 1

    num_moves += distance
    return num_moves


def simMany():

    global RUNS

    moves_num = 0

    for i in range(RUNS):

        moves = simOneRun()
        moves_num += moves

    return float(moves_num) / float(RUNS)


def main():

    global threshold_next

    for thresh in range(0,25+1):

        threshold_next = thresh
        result = simMany()

        print "Results for Threshold: {0}, {1} Moves on Avg".format(thresh, result)


main()
