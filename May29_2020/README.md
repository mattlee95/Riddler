# Riddler Classic : May 29th, 2020




## Problem Statement


From Jim Crimmins comes a puzzle about what would presumably be the largest Zoom meeting of all time:

One Friday morning, suppose everyone in the U.S. (about 330 million people) joins a single Zoom meeting between 8 a.m. and 9 a.m. — to discuss the latest Riddler column, of course. This being a virtual meeting, many people will join late and leave early.

In fact, the attendees all follow the same steps in determining when to join and leave the meeting. Each person independently picks two random times between 8 a.m. and 9 a.m. — not rounded to the nearest minute, mind you, but any time within that range. They then join the meeting at the earlier time and leave the meeting at the later time.

What is the probability that at least one attendee is on the call with everyone else (i.e., the attendee’s time on the call overlaps with every other person’s time on the call)?

Extra credit: What is the probability that at least two attendees are on the call with everyone else?


## Solution


For a Zoom call with 330 million participants all joining at times described in the problem statement the probability of each occurance is as follows:

`P(At least 1 caller is on call with every other caller) = 2/3`

`P(At least 2 callers are on call with every other caller) = 2/5`


## Solution Methodology (Normal and Extra Credit Problems)


This problem sticks out as the time I was most genuinely surprised by the mathematics/statistics behind one of these riddles.  I knew that my typical method of determining true probability by solving the problem over all permutations was not possible for a population of 330 million participants.

Knowing this I tried to calculate the true probability of the call for n = 2 all the way to n = 6 which seemed to be the limitation of my computer and my solution methodology. Luckily a pattern was evident that the probability of having one or more caller see everyone else on the call was always 2/3, no matter the size of n.  The same was true about the extra credit problem which, asides from n = 2 (for obvious reasons), all population sizes had the same proability of having 2+ callers see everyone else.

Just to do some further due diligance on the problem, I wrote up a Monte Carlo simulation for population sizes ranging from n = 2 to n = 99.  Each population size ran the simulation 1,000,000 times and the probabilities from the simulation backed up the pattern I was seeing on the all permuation calculations


## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
