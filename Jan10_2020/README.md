# Riddler Classic : Jan 10th, 2020




## Problem Statement

From Leonard Cohen comes a puzzle at the intersection of language and mathematics:

In Jewish study, “Gematria” is an alphanumeric code where words are assigned numerical values based on their letters. We can do the same in English, assigning 1 to the letter A, 2 to the letter B, and so on, up to 26 for the letter Z. The value of a word is then the sum of the values of its letters. For example, RIDDLER has an alphanumeric value of 70, since R + I + D + D + L + E + R becomes 18 + 9 + 4 + 4 + 12 + 5 + 18 = 70.

But what about the values of different numbers themselves, spelled out as words? The number 1 (ONE) has an alphanumeric value of 15 + 14 + 5 = 34, and 2 (TWO) has an alphanumeric value of 20 + 23 + 15 = 58. Both of these values are bigger than the numbers themselves.

Meanwhile, if we look at larger numbers, 1,417 (ONE THOUSAND FOUR HUNDRED SEVENTEEN) has an alphanumeric value of 379, while 3,140,275 (THREE MILLION ONE HUNDRED FORTY THOUSAND TWO HUNDRED SEVENTY FIVE) has an alphanumeric value of 718. These values are much smaller than the numbers themselves.

If we consider all the whole numbers that are less than their alphanumeric value, what is the largest of these numbers?

## Solution

The largest number with an alphanumeric sum greater than its value is:

    - 279 (TWO HUNDRED SEVENTY NINE) : Sum = 284

## Solution Methodology

Toughest part of this problem was writing a program that could translate an integer value into its corresponding english word.

In the solution you will see I divided the task of coverting int value into alphanumeric string by dividing by ones/thousands/millions.  Since the makeup of each 3 digits in a number will have the same alphanumeric word, with the addition of a suffix (thousand, million, billion).  Using this method I was able to cleanly write a program that to translate between the two representations.

After that, it was as simple as summing the alphanumeric values of the characters in the string and then comparing this sum to the true value of the number.
