# CS526 Homework Assignment 4

## Traversals

The written answers are in `traversal_answers.txt`. Both questions labeled
Problem 1 in the assignment are included.

## Problem 2: Smallest number of elements

Sort the values from largest to smallest, then add them until the sum is
strictly greater than T. The first count that reaches this condition is the
answer. The selected elements do not need to be next to each other.

For any count k, the k largest values have the greatest possible sum among
all selections of k elements. If their sum does not exceed T, no other
selection of k elements can exceed T. Therefore, the first successful count
is the minimum.

Time: O(n log n). Extra space: O(n) for the sorted copy.
The program reads integer values and assumes a solution exists, as stated
in the assignment. If T is negative, an empty selection is allowed and the
answer is 0.

Run in a terminal that supports input redirection (Command Prompt on Windows):

```text
python3 smallestNumber.py < smallest_input.txt
```

Output for the included input file:

```text
Input: 3,1,8,2,4,6,9,5 Target: 17 Answer: 3
```

For the separate example [8,3,9,2,7,1,5] and T = 18, the answer is also 3:
9 + 8 = 17, while 9 + 8 + 7 = 24 > 18.

## Problem 3: Unique right triangles

Use each point as a possible right-angle vertex. For every other point,
compute its direction from this vertex. Divide both components by their
greatest common divisor and use a consistent sign, so points on the same
line share a dictionary key. The direction perpendicular to (dx, dy) is
(-dy, dx), also normalized to the same sign convention.

The dictionary stores the number of earlier points in each direction.
For each new point, add the count in its perpendicular direction. Every
matching pair forms one right triangle with the current vertex.

Each pair is counted only when its second point is processed. A right
triangle has exactly one right-angle vertex, so it is counted exactly once
overall. Collinear triples are not counted. Integer direction pairs avoid
rounding errors and division by zero for vertical slopes.

Time: O(n^2) dictionary operations, with an additional O(log M) factor for
gcd, where M bounds coordinate differences. Extra space: O(n).
This avoids the O(n^3) approach of checking all triples. Actual runtime
depends on the number of points and the computer.

Input coordinates are assumed to be integers, as in the assignment's
example; points must be distinct as stated in the assignment.
Only the Python standard library is used.

```text
python3 rightTriangles.py < right_triangles_input.txt
```

Output:

```text
The number of right triangles is: 4
```

If your Windows installation uses `python` instead of `python3`, substitute
that command. In PowerShell, use these commands instead of `<`:

```powershell
Get-Content smallest_input.txt | python smallestNumber.py
Get-Content right_triangles_input.txt | python rightTriangles.py
```
