import random
import sys


def simulate_random_birthdays(num_people):

    '''
    Each index of birthdays_per_day will track number of people who have been
    randomly assigned to that birthday.

    Repeating this for the given group size (num_people) will simulate a
    random assortment of birthdays
    '''
    birthdays_per_day = [0] * 365

    for i in range(num_people):
        ind = random.randint(0,364)
        birthdays_per_day[ind] = birthdays_per_day[ind] + 1
 
    '''
    Return the number of birthdays for the day with most birthdays
    '''
    return max(birthdays_per_day)



def simulate_num_people(num_people, simulations):
    
    successes = 0

    '''
    Simulate random groups of birthdays for a group of given size (num_people)
    for a given number of simulations (simulations)
    '''
    for i in range(simulations):
        successes += simulate_random_birthdays(num_people) >= 3

    '''
    Return number of simulation which had a day with at least 3 birthdays in
    a day
    '''
    return successes



def gather_probs():

    NUM_SIMS = 1000 * 1000
    min_people = 85
    max_people = 90

    '''
    For every group size in the range specified by min_people and max_people
    run the number of simulations specified by NUM_SIMS

    Print rate at which those groups have a day which contains at least 3
    birthdays 
    '''
    for i in range(min_people, max_people+1):
        successes = simulate_num_people(i, NUM_SIMS)
        print "{0} group of people chance: {1}".format(i, float(successes)/float(NUM_SIMS))


gather_probs()
