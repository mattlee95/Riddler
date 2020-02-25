# Riddler Classic : February 21st, 2020




## Problem Statement

From Abijith Krishnan comes a game of coin flipping madness:

You have two fair coins, labeled A and B. When you flip coin A, you get 1 point if it comes up heads, but you lose 1 point if it comes up tails. Coin B is worth twice as much — when you flip coin B, you get 2 points if it comes up heads, but you lose 2 points if it comes up tails.

To play the game, you make a total of 100 flips. For each flip, you can choose either coin, and you know the outcomes of all the previous flips. In order to win, you must finish with a positive total score. In your eyes, finishing with 2 points is just as good as finishing with 200 points — any positive score is a win. (By the same token, finishing with 0 or −2 points is just as bad as finishing with −200 points.)

If you optimize your strategy, what percentage of games will you win? (Remember, one game consists of 100 coin flips.)

Extra credit: What if coin A isn’t fair (but coin B is still fair)? That is, if coin A comes up heads with probability p and you optimize your strategy, what percentage of games will you win?


## Solution

The optimal strategy for maximizing the probability of ending the coin game with a positive score is to use the 1-point coin whenever your score is greater than or equal to 0.  When your score is less than 0 use the 2-point coin.  Using this strategy the probability of winning the game is as follows:

`P(end game with positive score) = 0.640317447276`

Full results and extra credit solution for below.


## Solution Methodology 

Thinking about the problem initially I tried to visualize which cases I would want to use the 2-point coin to the 1-point coin.  Although the expected value of flipping each coin is the same the variance of the 2 coins are vastly different.  The solution came down to what scenarios would the optimal solution be low-variance play and which solutions would be high-variance play.

I speculated that when above 0 one would likely perfer to flip the low-variance coin as they are already above thier target value.  Conversely if the score is under 0, an optimal player would perfer to take a high-variance strategy.  Below you will find crude figures of what I though about.  See how the 2-point distribution has far more or the distrubution on the other end of the score threshold.  When under the threshold this represents a positive, but when above the threshold this is a negative.

![Image: Positive Distributions](https://github.com/mattlee95/Riddler/blob/master/Feb21_2020/figures/coinGame/coinGame.002.jpeg)

![Image: Negative Distributions](https://github.com/mattlee95/Riddler/blob/master/Feb21_2020/figures/coinGame/coinGame.001.jpeg)

I wrote a program [coinFlip.py](https://github.com/mattlee95/Riddler/blob/master/Feb21_2020/coinFlip.py) in order to test this threshold as well as other thresholds to make sure that the positve/negative strategy was indeed the optimal.


## Solution (Extra Credit)

For the extra credit problem we were taked with solving the same game for solutions in which the 1-point coin was not fair.  I computed the best strategy and odds for probability of heads decrementing by 5% from 50%.

In these solutions you will see the optimal strategy represented by an array of High Variance to Low Variance thresholds.  These arrays represent the score you must have in order to switch from using the 2-point coin to the 1-point coin.

For example, given array `[1,2,3,4]`, before turn 1 if you score is greater than array{0} (array{turn-1}) then you would use the 1-point coin otherwise you would use the 2-point coin:

|P(heads) for 1-point coin|Optimized P(win)|Optimal Threshold|
|--|--|--|
|`0.45`|`0.555342733959`|`[1, 3, 5, 7, 9, 11, 12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 12, 13, 10, 11, 12, 13, 12, 13, 10, 11, 12, 13, 10, 9, 10, 11, 12, 9, 10, 11, 8, 9, 10, 11, 8, 9, 10, 9, 10, 9, 10, 9, 10, 9, 8, 9, 6, 7, 8, 9, 6, 7, 8, 7, 8, 5, 6, 7, 6, 7, 6, 7, 4, 5, 6, 5, 6, 5, 6, 5, 6, 5, 4, 5, 4, 5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 2, 3, 2, 3, 2, 1]`
|`0.4`|`0.527917279748`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20, 21, 20, 21, 20, 21, 20, 21, 22, 21, 22, 23, 20, 21, 20, 21, 20, 21, 18, 19, 20, 21, 20, 21, 18, 17, 18, 19, 16, 17, 18, 17, 18, 17, 18, 17, 14, 15, 16, 17, 14, 13, 14, 15, 12, 13, 14, 13, 14, 13, 12, 13, 10, 11, 12, 9, 10, 11, 8, 9, 10, 9, 10, 9, 10, 9, 8, 9, 6, 7, 8, 7, 6, 7, 6, 7, 4, 5, 6, 5, 4, 5, 4, 3, 4, 3, 2, 3, 2, 1]`
|`0.35`|`0.51377721791`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 28, 29, 28, 29, 30, 31, 32, 33, 32, 33, 28, 29, 28, 29, 28, 29, 28, 29, 28, 29, 26, 25, 24, 25, 26, 25, 24, 25, 22, 23, 24, 21, 20, 21, 22, 21, 22, 21, 20, 21, 18, 17, 18, 19, 16, 17, 18, 17, 18, 17, 14, 15, 16, 13, 12, 13, 14, 13, 14, 13, 10, 11, 12, 9, 10, 11, 8, 9, 8, 9, 8, 9, 6, 7, 6, 5, 6, 5, 4, 5, 4, 3, 4, 3, 2, 1]`
|`0.3`|`0.50875881508`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 36, 37, 36, 37, 36, 37, 36, 37, 36, 37, 36, 37, 36, 37, 36, 37, 36, 33, 32, 33, 32, 33, 32, 33, 30, 29, 28, 29, 28, 29, 28, 29, 26, 25, 24, 25, 24, 25, 22, 21, 22, 23, 20, 21, 22, 21, 20, 21, 18, 17, 18, 17, 18, 17, 16, 17, 14, 13, 14, 13, 12, 13, 12, 13, 10, 9, 10, 9, 8, 9, 8, 7, 6, 7, 6, 5, 4, 5, 4, 3, 2, 1]`
|`0.25`|`0.506687550325`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 44, 45, 44, 45, 44, 45, 44, 45, 44, 41, 40, 41, 40, 41, 40, 41, 40, 37, 36, 37, 36, 37, 36, 37, 34, 33, 32, 33, 32, 33, 30, 29, 28, 29, 28, 29, 26, 25, 26, 25, 26, 25, 24, 25, 22, 21, 20, 21, 20, 21, 18, 17, 18, 17, 16, 17, 14, 13, 14, 13, 12, 13, 10, 11, 10, 9, 8, 9, 8, 7, 6, 5, 6, 5, 4, 3, 2, 1]`
|`0.2`|`0.506974863758`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 52, 53, 52, 49, 48, 49, 48, 49, 48, 45, 44, 45, 44, 45, 44, 41, 40, 41, 42, 41, 40, 41, 38, 37, 36, 37, 36, 33, 32, 33, 32, 33, 32, 29, 28, 29, 28, 29, 26, 25, 26, 25, 24, 25, 22, 21, 22, 21, 20, 21, 18, 17, 16, 17, 16, 13, 14, 13, 12, 13, 12, 11, 10, 9, 8, 9, 6, 7, 6, 5, 4, 3, 2, 1]`
|`0.15`|`0.506642876577`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 56, 57, 56, 57, 56, 53, 52, 53, 52, 49, 48, 49, 48, 49, 48, 45, 44, 45, 44, 45, 44, 41, 40, 41, 40, 37, 36, 37, 36, 37, 36, 33, 32, 33, 32, 29, 28, 29, 28, 29, 26, 25, 26, 25, 24, 23, 22, 21, 20, 21, 18, 17, 18, 17, 16, 15, 14, 13, 12, 13, 10, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`
|`0.1`|`0.507009280895`|`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 60, 61, 60, 61, 60, 57, 56, 57, 56, 53, 52, 53, 52, 49, 48, 49, 48, 49, 48, 45, 44, 45, 44, 41, 40, 41, 40, 37, 38, 37, 36, 37, 34, 33, 32, 33, 32, 29, 28, 29, 28, 25, 26, 25, 24, 23, 22, 21, 20, 21, 18, 17, 16, 17, 16, 13, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`
|`0.05`|`0.507043612639`|`[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 66, 65, 62, 61, 60, 61, 58, 57, 56, 57, 56, 57, 54, 53, 52, 53, 50, 49, 48, 49, 46, 45, 44, 45, 42, 41, 40, 41, 38, 37, 36, 37, 34, 33, 32, 33, 30, 29, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 2]`
|`0`|`0.507046877512`|`[3, 0, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 68, 67, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 35, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 2]`


## Solution Methodology (Extra Credit)

For the extra credit solution found in [coinFlipExtra.py](https://github.com/mattlee95/Riddler/blob/master/Feb21_2020/coinFlipExtra.py) I just repurposed the orignal solution and wrapped it around a program which incremented thresholds by index until the optimal solution for that threshold was found.  By looking at the thresholds and the probabilities it seems like this method did not find the absolute optimal solutions, but today was a busy week at work and I dont have time to figure out a new optimization.


## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
