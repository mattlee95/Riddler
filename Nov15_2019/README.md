# Riddler Classic : Novmeber 15th, 2019




## Problem Statement

From Ricky Jacobson comes a puzzle of seeing how low you can roll:

You are given a fair, unweighted 10-sided die with sides labeled 0 to 9 and a sheet of paper to record your score. (If the very notion of a fair 10-sided die bothers you, and you need to know what sort of three-dimensional solid it is, then forget it — you have a random number generator that gives you an integer value from 0 to 9 with equal probability. Your loss — the die was a collector’s item.)

To start the game, you roll the die. Your current “score” is the number shown, divided by 10. For example, if you were to roll a 7, then your score would be 0.7. Then, you keep rolling the die over and over again. Each time you roll, if the digit shown by the die is less than or equal to the last digit of your score, then that roll becomes the new last digit of your score. Otherwise you just go ahead and roll again. The game ends when you roll a zero.

For example, suppose you roll the following: 6, 2, 5, 1, 8, 1, 0. After your first roll, your score would be 0.6, After the second, it’s 0.62. You ignore the third roll, since 5 is greater than the current last digit, 2. After the fourth roll, your score is 0.621. You ignore the fifth roll, since 8 is greater than the current last digit, 1. After the sixth roll, your score is 0.6211. And after the seventh roll, the game is over — 0.6211 is your final score.

What will be your average final score in this game?

## Solution

If the vizier strategizes as outlined below she can expect to choose the candidate with an average rank of 2.55793650794

Full list of average ranks during the optimization process can be found at solution.txt

The optimal strategy in this scenario would be:

    1. Reject the first 3 candidates

    2. If the 4th candidate ranks 1st among those rejected, select the 4th candidate, else reject

    3. If the 5th candidate ranks 1st among those rejected, select the 5th candidate, else reject

    4. If the 6th candidate ranks either 1st or 2nd among those rejected, select the 6th candidate, else reject

    5. If the 7th candidate ranks either 1st or 2nd among those rejected, select the 7th candidate, else reject

    6. If the 8th candidate ranks either 1st, 2nd or 3rd among those rejected, select the 8th candidate, else reject

    7. If the 9th candidate ranks either 1st, 2nd, 3rd or 4th among those rejected, select the 9th candidate, else reject

    8. If you have rejected all other candidate select the 10th (final) candidate

## Solution Methodology

I solved this problem by first creating a function that took rules for selecting a candidate and used those rules to give an average outcome for all possible permutations.  The inputs were REJECT_UNTIL or how many candidates to initially automatically reject and THRESHOLD which represented how high a candidate at that point in the process must rank compared to those rejected in order to be selected.

Utilizing this function I was able to write a higher level function that changed values of both the REJECT_UNTIL and THRESHOLD parameters to optimize the rules to select the lowest average rank.

In order to demonstrate the logic, take the following example:
- Candidates ordered `[1, 9, 3, 7, 4, 6, 2, 5, 8, 10]`
- `REJECT_UNTIL = 3`, representing the first 3 candidates will always be rejected
- `THRESHOLD = [0, 0, 0, 0, 0, 1, 1, 2, 3]`, specifying which rejected candidate each new candidate will be compared to.

|  |Reject (Sorted) |Order of Next Appearance |Threshold  |Decision|
|--|--|--|--|--|
|Step 0  |[]  |[1, 9, 3, 7, 4, 6, 2, 5, 8, 10]  |[__0__, __0__, __0__, 0, 0, 1, 1, 2, 3]|  Reject 1, 9, 3
|Step 1  |[__1__, 3, 9]  |[__7__, 4, 6, 2, 5, 8, 10]  |[0, 0, 0, __0__, 0, 1, 1, 2, 3]|  1 < 7, Reject 7
|Step 2  |[__1__, 3, 7, 9]  |[__4__, 6, 2, 5, 8, 10]  |[0, 0, 0, 0, __0__, 1, 1, 2, 3]|  1 < 4, Reject 4
|Step 3	 |[1, __3__, 4 , 7, 9]  |[__6__, 2, 5, 8, 10]  |[0, 0, 0, 0, 0, __1__, 1, 2, 3]|  3 < 6, Reject 6
|Step 4  |[1, __3__, 4, 6, 7, 9]  |[__2__, 5, 8, 10]  |[0, 0, 0, 0, 0, 1, __1__, 2, 3]|  3 > 2, Accept 2

The Function will return candidate of rank `2` in this example


Please see the source code and comments in sultanSim.py for a more in depth description of the functions and algorithms used to optimize the parameters of candidate selection.

## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
