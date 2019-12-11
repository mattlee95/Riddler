# Riddler Classic : December 5th, 2019




## Problem Statement

From Austin Chen comes a riddle of efficiently finding a song:

You have a playlist with exactly 100 tracks (i.e., songs), numbered 1 to 100. To go to another track, there are two buttons you can press: (1) “Next,” which will take you to the next track in the list or back to song 1 if you are currently on track 100, and (2) “Random,” which will take you to a track chosen uniformly from among the 100 tracks. Pressing “Random” can restart the track you’re already listening to — this will happen 1 percent of the time you press the “Random” button.

For example, if you started on track 73, and you pressed the buttons in the sequence “Random, Next, Random, Random, Next, Next, Random, Next,” you might get the following sequence of track numbers: 73, 30, 31, 67, 12, 13, 14, 89, 90. You always know the number of the track you’re currently listening to.

Your goal is to get to your favorite song (on track 42, of course) with as few button presses as possible. What should your general strategy be? Assuming you start on a random track, what is the average number of button presses you would need to make to reach your favorite song?


## Solution

The strategy that will result in the fewest button presses as possible is to press the "Random" button until you are within 13 "Next" button presses of the desired song. 

For this strategy `Expected Moves = 12.6428571429`


## Solution Methodology

For this solution I was operating under the intutition that the best strategy would be cases which defined when to press "Random" vs "Next".  Since each random selection was independent of one another this case would remain constant throughout the scenario.

I began by creating a simple Python script <em>songSkipSim.py</em> in order to simulate the problem to get a good idea of the range I was going to be looking at.

The script gave me a pretty good idea I was looking at the optimal strategy being use "Random" when further than the threshold "Next" clicks away otherwise using "Next" where the threshold was in the range of 10 - 15.
  
I recognized for the case of X = 0 (Use "Random" until desired song is reached) we would be dealing with a standard geometric distribution with a probability of 1 / 100.  Using the summation representation of a geometric distribution, I was able to write an formula for the expected number of moves for any threshold value.

![Image: Summation Formula](https://github.com/mattlee95/Riddler/blob/master/Dec5_2019/summationFormula.png)

![Graph: Relationship Between Threshold and Expected Moves](https://github.com/mattlee95/Riddler/blob/master/Dec5_2019/100SongsFull.png)

## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
