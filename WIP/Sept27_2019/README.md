# Riddler Classic : Sept 13th, 2019 




## Problem Statement

"Recent Riddlers have tackled  [Scrabble Superstrings](https://fivethirtyeight.com/features/whats-your-best-scrabble-string/)  and  [road trips through 48 states](https://fivethirtyeight.com/features/can-you-escape-this-enchanted-maze/). For this week’s Riddler Classic, Max Maguire combines these two puzzles into one:

The challenge is to find the longest string of letters in which (1) every pair of consecutive letters is a two-letter state or territory abbreviation, and (2) no state abbreviation occurs more than once. For example, Guam, Utah and Texas can be combined into the valid four-letter string GUTX. Another valid string is ALAK (Alabama, Louisiana and Alaska), while ALAL (Alabama, Louisiana and Alabama) is invalid because it includes the same state, Alabama, twice.

For reference, the full list of abbreviations is available  [here](https://pe.usps.com/text/pub28/28apb.htm), courtesy of the United States Postal Service."

## Solution

There are 9984 unique strings of length 31 (30 states used) all of which begin with the Federated States of Micronesia (FM) and end in an abbreviation ending in "E"

A list of these solutions can be found in solution.txt

## Solution Methodology

I think of this solution as a breadth first computation down a tree containing nodes of:
[("current string", [list of unused states]), ...]

For each legal string that can be created for each node we add that to a list of nodes in the next level: 
[("current string + legal state", [list of unused states - legal state just added]), ...]

We continue until we reach a level which cannot be populated with legal additions to the strings.
