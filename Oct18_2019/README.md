# Riddler Classic : October 18th, 2019 




## Problem Statement

"From Michael Branicky, a challenge of currency conversion:

Riddler Nation has two coins: the Dio, worth $538, and the Phantus, worth $19. When visiting on vacation, Riddler National Bank will gladly convert your dollars into Dios and Phanti. For example, if you were to give a bank teller $614, they’d return to you one Dio and four Phanti, since 614 = 1 × 538 + 4 × 19. But if you tried to exchange one dollar more (i.e., $615), then alas, there is no combination of Dios and Phanti the teller could give you, and you won’t get your money’s worth in local currency.

To make the bank teller’s job (and your vacation) as miserable as possible, you decide to bring the largest dollar amount that cannot be converted into Riddler currency. How much money are we talking here? That is, what’s the largest whole number that cannot be expressed as a sum of 19s and 538s?

Extra Credit: Word is that Riddler Nation is considering minting a third currency, worth $101. If they do, then what would be the largest dollar amount that cannot be converted into Riddler currency?"

## Solution

For Currency Denominations of $19 and $538, the highest value that cannot be created is $9665

Full list of values and divisibility can be found in solution_19_538.log


For Currency Denominations of $19, $101 and $538, the highest value that cannot be created is $1799

Full list of values and divisibility can be found in solution_19_101_538.log

## Solution Methodology

I solved this problem by created a program in python to determine whether or not a value was divisible by a set of denominations.
Going off of this function I knew that once I found 19 consecutive values that were divisible all other values would be divisible since $19 was the smallest denomination of curreny
The program interates up from 0 until it find 19 values in a row that are divisible and prints the last indivisible value it encountered.

A more in-depth explaination of the algorithm can be found in riddlerCurrency.py

I could not help but noticing for both instances the highest indivisible value could be calculated using the formula:

Highest Indivisible = ((second lowest denomination) / (lowest denomination - 1)) - lowest denomination

9665 = ((538) / (19 - 1)) - 19

1799 = ((101) / (19 - 1)) - 19
