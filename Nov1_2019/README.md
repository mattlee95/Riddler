# Riddler Classic : Novmeber 1st, 2019




## Problem Statement

From Julien Beasley, a new spin on the Sultan’s Dowry Problem, a classic problem of matrimony:

The sultan has asked her vizier to present her with 10 candidates for marriage. The vizier has searched the kingdom for the 10 most desirable partners, but he does not know whom the sultan will prefer. If she saw them all at the same time, she would easily be able to rank them from 1 (the best partner) to 10 (the worst partner). But the vizier can only present the candidates one at a time — very hard to sync everybody’s calendars, even back then — and in a random order. Upon seeing each candidate, the sultan must reject or accept him. If a candidate is rejected, the sultan cannot pick him again. But on seeing each new candidate, she knows exactly where he’d stack up relative to the candidates she has rejected. If she strategizes, what’s the highest rank she can expect her chosen candidate to have on average?

For example, if she simply accepted the first candidate presented to her, his rank could be anywhere from 1 to 10 with equal probability, averaging to 5.5. Surely she can do better…

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

Please see the source code and comments in sultanSim.py for a more in depth description of the functions and algorithms used to optimize the parameters of candidate selection.

## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
