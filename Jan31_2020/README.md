# Riddler Classic : January 31st, 2020




## Problem Statement

From Robert Berger comes a question of maximizing magnetic volume:

Robert’s daughter has a set of Magna-Tiles, which, as their name implies, are tiles with magnets on the edges that can be used to build various polygons and polyhedra. Some of the tiles are identical isosceles triangles with one 30 degree angle and two 75 degree angles. If you were to arrange 12 of these tiles with their 30 degree angles in the center, they would lay flat and form a regular dodecagon. If you were to put fewer (between three and 11) of those tiles together in a similar way, they would form a pyramid whose base is a regular polygon. Robert has graciously provided a photo of the resulting pyramids when three and 11 tiles are used:

![Image: Riddler Image](https://fivethirtyeight.com/wp-content/uploads/2020/01/pyramids.png?w=1150)

3 magnatiles arranged into a tall pyramid, and 11 magnatiles arranged into a short pyramid.
If Robert wanted to maximize the volume contained within the resulting pyramid (presumably to store as much candy for his daughter as possible), how many tiles should he use?


## Solution

The number of triangle manga tiles that create a pyramid shape with the greatest volume is 9.  Under the assumption that the base of these magna tiles is 10 units long the volume is as follows:

`Volume of Shape of 9 tiles = 2543.03984026`

Full results for all shapes below.


## Solution Methodology

For this solution the difficult part was determining a methmod to find the volume of the pyramid shapes created by a certain number of the triangle magna tiles.  To begin I started by isolating the problem to solving for the volume of an individual slice and then multiplying that volume by the corresponding number of slices in the shape.

Narrowing the problem down further I found that the majority of the problem was solving for the dimensions of two of the triangles of the triangular based pyramid slice.  The two triangles were the actual manga tile traingle and what I called the base triangle (think of this as the triangular shadow cast when the magna tile is leaning into the shape.


### Magna Tile Triangle

For the magna tile triangle I gave some placeholder for the dimensions so I would have an acutal value for each calculated volume.  I chose to make the base of the triangle 10 units long.  This in turn, since it is a 75, 75, 30 isoceles triangle make the height of the tile 18.66 units long.

![Image: Magna Tile Triangle Diagram](https://github.com/mattlee95/Riddler/blob/master/Jan31_2020/diagrams/diagramMagna.gif)


### Base Triangle

For the base triangle, I was able to take the base value of the manga tile triangle and use it for the base as well.  I was able to determine the angles of the triangle based on the regular polygon formed when making a pyramid of n triangular tiles.

`base angle = (180deg * (num_slices - 2) / (num_slices)) / 2`

Using this angle I was then able to calculate the height of the base triangle using the formula

`base height = (base / 2) / cos(base angle)`

Then using the base height and the height of the tile we can calculate the height of the pyramid using the formula

`pyramid height = magna height * cos(sin-1(base height / magna height))`

![Image: Base Triangle Diagram](https://github.com/mattlee95/Riddler/blob/master/Jan31_2020/diagrams/diagramBase.gif)

Finally I calculated the volume of a slice and therefore the entire bowl using the formula

`base area = magna base * base height / 2`

`slice volume = base area * pyramid height / 3`

`bowl volume = slice volume * number of tiles`

The results of using a number of traingles from 3 - 11 is as follows:

`Bowl of 3 slices has volume of 512.243103686`

`Bowl of 4 slices has volume of 814.050135042`

`Bowl of 5 slices has volume of 1177.34038382`

`Bowl of 6 slices has volume of 1575.45209404`

`Bowl of 7 slices has volume of 1965.23232794`

`Bowl of 8 slices has volume of 2317.25951908`

`Bowl of 9 slices has volume of 2543.03984026`

`Bowl of 10 slices has volume of 2506.66968821`

`Bowl of 11 slices has volume of 2340.83769464`


## Self-promoting Plug

I am currently a software engineer in the San Francisco Bay Area who is open to chatting about exciting software engineering, data science and firmware development roles.  Feel free to take a look at my resume in the top level of this repository and shoot me an email/LinkedIn message if you have an interesting position that you would like to chat about.
