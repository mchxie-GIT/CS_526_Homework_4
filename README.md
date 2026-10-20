## Problem 1

The answers are in `Problem 1.txt`.

## Problem 2

Sort the values from largest to smallest, then add them until the sum is 
greater than T. The first count that reaches this condition is the
answer.

For any count k, the k largest values have the greatest possible sum among
all selections of k. If their sum is less than T, no other
k elements can exceed T. Therefore, the first successful count
is the min.

If T is negative, an empty selection is allowed and the
answer is 0.

Run in a terminal that supports input redirection.

For the separate example [8,3,9,2,7,1,5] and T = 18, the answer is also 3:
9 + 8 = 17, while 9 + 8 + 7 = 24 > 18.

## Problem 3

Use each point as a possible right-angle vertex. For every other point,
compute its direction from this vertex. Divide both components by their
greatest common divisor and use a consistent sign, so points on the same
line share a dictionary key. The direction perpendicular to (dx, dy) is
(-dy, dx), also normalized to the same sign convention.

The dictionary stores the number of earlier points in each direction.
For each new point, add the count in its perpendicular direction. Every
matching pair forms one right triangle with the current vertex.

Each pair is counted only when its second point is processed. A right
triangle has exactly one right-angle vertex, so it is counted once
overall. Collinear triples are not counted. Integer direction pairs avoid
rounding errors and division by zero for vertical slopes.
