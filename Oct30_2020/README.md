# Riddler Classic : Oct 2nd, 2020 




## Problem Statement

From mathematician (and author of Basic Probability: What Every Math Student Should Know) Henk Tijms comes a choice matter of chance and chocolate:

I have 10 chocolates in a bag: Two are milk chocolate, while the other eight are dark chocolate. One at a time, I randomly pull chocolates from the bag and eat them — that is, until I pick a chocolate of the other kind. When I get to the other type of chocolate, I put it back in the bag and start drawing again with the remaining chocolates. I keep going until I have eaten all 10 chocolates.

For example, if I first pull out a dark chocolate, I will eat it. (I’ll always eat the first chocolate I pull out.) If I pull out a second dark chocolate, I will eat that as well. If the third one is milk chocolate, I will not eat it (yet), and instead place it back in the bag. Then I will start again, eating the first chocolate I pull out.

What are the chances that the last chocolate I eat is milk chocolate?

## Solution

The Probability of selecting a certain type of chocolate as the last peice is as follows:

`P(milk) = 0.5, P(dark) = 0.5`

## Solution Methodology

For permutational statistics problems like this I like to use a psuedo tree down method of solving where I don't necessarily care about each nodes connections, rather the level on the tree it occupies.

For full commented source code for this solution please see [ChocolateBag.py](https://github.com/mattlee95/Riddler/blob/master/Oct2_2020/ChocolateBag.py)
