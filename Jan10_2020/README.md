# Riddler Classic : Jan 10th, 2020




## Problem Statement


## Solution

The largest number with an alphanumeric sum greater than its value is:

    - 279 (TWO HUNDRED SEVENTY NINE) : Sum = 284

## Solution Methodology

Toughest part of this problem was writing a program that could translate an integer value into its corresponding english word.

In the solution you will see I divided the task of coverting int value into alphanumeric string by dividing by ones/thousands/millions.  Since the makeup of each 3 digits in a number will have the same alphanumeric word, with the addition of a suffix (thousand, million, billion).  Using this method I was able to cleanly write a program that to translate between the two representations.

After that, it was as simple as summing the alphanumeric values of the characters in the string and then comparing this sum to the true value of the number.
