# Riddler Classic : Jan 3rd, 2020




## Problem Statement

The New York Times recently launched some new word puzzles, one of which is Spelling Bee. In this game, seven letters are arranged in a honeycomb lattice, with one letter in the center. Here’s the lattice from December 24, 2019:

Spelling Bee screenshot, with the required letter G, and the additional letters L, A, P, X, M and E.
The goal is to identify as many words that meet the following criteria:

The word must be at least four letters long.
The word must include the central letter.
The word cannot include any letter beyond the seven given letters.
Note that letters can be repeated. For example, the words GAME and AMALGAM are both acceptable words. Four-letter words are worth 1 point each, while five-letter words are worth 5 points, six-letter words are worth 6 points, seven-letter words are worth 7 points, etc. Words that use all of the seven letters in the honeycomb are known as “pangrams” and earn 7 bonus points (in addition to the points for the length of the word). So in the above example, MEGAPLEX is worth 15 points.

Which seven-letter honeycomb results in the highest possible game score? To be a valid choice of seven letters, no letter can be repeated, it must not contain the letter S (that would be too easy) and there must be at least one pangram.

For consistency, please use this word list to check your game score.2


## Solution

The seven letter honeycomb that resutls in the highest possible game score with the following conditions:

    - No repeated letters

    - Letter 's' cannot be used

    - Group of letters must have at least one pangram


Letters = ('a', 'e', 'g', 'i', 'n', 'r', 't')

Middle Letter = t

Score = 3898


## Solution Methodology

Used a brute force approach for this solution solving for all permutations of all letters with the exception to 's', while tracking the maxinum score that satisfied the conditions

Taking a look at other submissions, optimized solutions were similar to my implimentation, with the exception that they took all works with exactly 7 unique letters and created thier permutations based on those sets.  This drastically cut down on the number of permutations that needed to be tested and in effect tested for the condition of needing at least one pangram in the beginning.
