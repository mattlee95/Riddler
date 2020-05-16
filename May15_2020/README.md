# Riddler Classic : February 21st, 2020




## Problem Statement


Since it was impossible to complete the game of sudoku, you might instead enjoy passing the time with a game of Dungeons & Dragons, courtesy of Emma Knight:

The fifth edition of Dungeons & Dragons introduced a system of “advantage and disadvantage.” When you roll a die “with advantage,” you roll the die twice and keep the higher result. Rolling “with disadvantage” is similar, except you keep the lower result instead. The rules further specify that when a player rolls with both advantage and disadvantage, they cancel out, and the player rolls a single die. Yawn!

There are two other, more mathematically interesting ways that advantage and disadvantage could be combined. First, you could have “advantage of disadvantage,” meaning you roll twice with disadvantage and then keep the higher result. Or, you could have “disadvantage of advantage,” meaning you roll twice with advantage and then keep the lower result. With a fair 20-sided die, which situation produces the highest expected roll: advantage of disadvantage, disadvantage of advantage or rolling a single die?

Extra Credit: Instead of maximizing your expected roll, suppose you need to roll N or better with your 20-sided die. For each value of N, is it better to use advantage of disadvantage, disadvantage of advantage or rolling a single die?


## Solution


The expected rolls for each of the given rolling conditions are as follows: `Disadvantage of Advantage: 11.1667`, `Advantage+Disadvantage (Single Dice): 10.5`, `Advantage of Disadvantage: 9.83334`

Extra credit: If you need to roll a value at or above N the best dice rolling condition is as follows: For a value of N between 2 and 13 your best condition is rolling `Disadvantage of Advantage`.  For values of N between 14 and 20 your best conditon is rolling `Advantage+Disadvantage (Single Dice)`

Solutions explained below

## Solution Methodology 

Pretty straight forward brute force solution.  You'll see in the [code](https://github.com/mattlee95/Riddler/blob/master/May15_2020/diceAdvantages.cpp) that I am just using nested for loops from 1-20 to represent the values of each of the dice.  This means for the 4 roll conditions I'm using 4 nested loops, but I had a hard time trying to figure out am more effient way of getting an exact value for the expected value under these conditions.  Below are the expected values for each of the 5 conditons mentioned in the problem statement.

`Advantage: 13.825`
`Disadvantage: 7.175`
`Advantage+Disadvantage (Single Dice): 10.5`
`Advantage of Disadvantage: 9.83334`
`Disadvantage of Advantage: 11.1667`


## Solution Methodology (Extra Credit)

Based on the structure of my program used to calculate the expected value all of the information needed to solve for the probability of rolling at or above any given number was already there.

The full rundown of the probabilities for scoring at or above every value can be found in [output.log](https://github.com/mattlee95/Riddler/blob/master/May15_2020/output.log), but for the sake of making this easy to buzz over in the README I plotted the 3 conditions the problem statement asked to compare.

Below in the graph you will see the probabilities graphed against one another.  Since the legend didnt copy over `Red: Disadvantage of Advantage`, `Green: Advantage of Disadvantage` and `Blue: Advantage+Disadvantage (Single Dice)`

![Image: Conditions Probability Plot](https://github.com/mattlee95/Riddler/blob/master/May15_2020/figure_1.png)


## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
