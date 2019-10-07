# Riddler Classic : October 4th, 2019 




## Problem Statement

"From Joel Lewis, this week’s Riddler Classic is a birthday puzzle for the ages:

The classic birthday problem asks about how many people need to be in a room together before you have better-than-even odds that at least two of them have the same birthday. Ignoring leap years, the answer is, paradoxically, only 23 people — fewer than you might intuitively think.

But Joel noticed something interesting about a well-known group of 100 people: In the U.S. Senate, three senators happen to share the same birthday of October 20: Kamala Harris, Brian Schatz and Sheldon Whitehouse.

And so Joel has thrown a new wrinkle into the classic birthday problem. How many people do you need to have better-than-even odds that at least three of them have the same birthday? (Again, ignore leap years.)"

## Solution

A group size of 88 is the smallest sized group that has greater than a 50% chance of having at least 3 members share the same birthday.

Other Notable Triple Birthday Probabilities:

 - Senate (n = 100) : P = .645864
 - House of Representatives (n = 435) : P = ~1.000000
 - Group with better than even odds for 2 birthdays shared (n = 23) : P = .012705

A list of probabilities for group sizes from 1 to 731 can be found in solution.txt

## Solution Methodology

I employeed 2 methods of determining the group size at which you are greater than 50% likely to have a triple pair of birthdays: Simulation and Calculating the true probabilities

triple_birthday_simulate.py

For the methodology for simulating, I simulated each group size 1,000,000 times to determine close to the true probability for each group size.  Using this method I was able to determine a group size of 88 was the first point at which the probability was >50%


triple_birthday_statistics.py

For the methodology of calculating the true probabilities, I created a tree for all permutations of groups increasing in size 1 until the max size of 731.  A list off all the probabilities can be found it solution.txt.  Comments in triple_birthday_statistics.py describes the algorithm used to calculate the probabilities

