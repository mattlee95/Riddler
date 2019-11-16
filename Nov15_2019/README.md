# Riddler Classic : Novmeber 15th, 2019




## Problem Statement

From Ricky Jacobson comes a puzzle of seeing how low you can roll:

You are given a fair, unweighted 10-sided die with sides labeled 0 to 9 and a sheet of paper to record your score. (If the very notion of a fair 10-sided die bothers you, and you need to know what sort of three-dimensional solid it is, then forget it — you have a random number generator that gives you an integer value from 0 to 9 with equal probability. Your loss — the die was a collector’s item.)

To start the game, you roll the die. Your current “score” is the number shown, divided by 10. For example, if you were to roll a 7, then your score would be 0.7. Then, you keep rolling the die over and over again. Each time you roll, if the digit shown by the die is less than or equal to the last digit of your score, then that roll becomes the new last digit of your score. Otherwise you just go ahead and roll again. The game ends when you roll a zero.

For example, suppose you roll the following: 6, 2, 5, 1, 8, 1, 0. After your first roll, your score would be 0.6, After the second, it’s 0.62. You ignore the third roll, since 5 is greater than the current last digit, 2. After the fourth roll, your score is 0.621. You ignore the fifth roll, since 8 is greater than the current last digit, 1. After the sixth roll, your score is 0.6211. And after the seventh roll, the game is over — 0.6211 is your final score.

What will be your average final score in this game?

## Solution

Some of the permutations of this problem continue infinitely, so the average final score will continue to reach the true value as you calculate the value more percisely.  The closest I was able to come was an average final score of `0.473684208945`


## Solution Methodology

My methodology for this solution was to track all possible scenarios, the value associated with them and the probability this scenario would occur.

Since the permutations of this problem can continue infintely, I needed a way of capping the amount of permutations I would let happen.  To do this I implemented a threshold for the probability a scenario must have for me to further calculate its permuations.  As I lowered the threshold, the longer the calculations took and the closer the program came to the true average value.


|Threshold Probability | Average Value |
|--|--|
|.1  |0.45  |
|.01  |0.472137926986  |
|.001  |0.473500712245  |
|.0001	|0.473666164011  |
|.00001  |0.473682468489  |
|.000001  |0.47368404281   |
|.0000001  |0.473684192884  |
|.00000001  |0.473684208945  |


Please see the source code and comments in 10sided.py for a more in depth description of the functions and algorithms used to calculate this scenarios average value.

## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
