"""
In the magical 2-dimensional world everything has a position on the ground and a height.
You are the head of the forestry department and you are teaching the new wood cutters.
With your experience and tenure comes wisdom. You know very well how hard it is to cut a tree, let alone an entire forest.
The trick is when a tree falls and touches another, that tree also falls.
Do it right and you will have a chain reaction.

You are given the numberOfTrees in the forest, each with it's position and height.
When a tree is cut down it always falls to the right.
Trees don't have widths so they stack on the ground indefinitely.
A tree knocks over another one when any point of the first tree during fall touches any point of the second tree above it's trunk (the point where it touches the ground).
One tree can knocks out few trees to the right, if its tall enough and trees to the right are close enough!!!
Output the minimum number of trees need to be cut down for the deforestation.

Example: You are given numberOfTrees = 3 trees with (1, 1), (3, 4), (6, 2) as their (position, height) pairs.
The forest looks like this (except trees touch the ground).



  │
  │
  │  │
│ │  │
───────
123456


When you cut down the first tree it won't touch the second one, so that's your first cut.
But when you cut down the second one it will knock down the third. So you have to cut 2 trees and you are finished.

Example 2: You have 2 trees with with (1, 2) and (3, 2) as their (position, height) pairs.
When you cut the first tree, the fallen tree will occupy the space between 1 and 3 precisely and therefore not touch the second tree above it's trunk.
You need 2 cuts for complete deforestation in this case.
Input
Line 1: numberOfTrees, an integer denoting the number of trees in the forest.
Next numberOfTrees Lines: position and height, two space separated integer for position of the tree on the ground and it's height. Input is ordered by position.
Output
The minimum number of trees to be cut down for all the trees to fall.
Constraints
2 ≤ numberOfTrees ≤ 100
0 ≤ position, height ≤ 100
Example

Input

3
1 1
3 4
6 2

Output

2




----test2------------


8
10 4
13 2
20 25
24 3
29 4
33 2
41 5
60 2


3


___test 3_________________

25
1 8
4 8
7 8
10 8
13 8
16 8
19 8
22 8
25 8
28 8
31 8
34 8
37 8
40 8
43 8
46 8
49 8
52 8
55 8
58 8
61 8
64 8
67 8
70 8
73 8

1


__________test4________

42
4 4
5 4
7 1
9 1
10 4
13 1
15 4
19 2
21 2
25 2
29 1
31 2
34 2
37 2
40 3
42 2
45 1
46 1
47 1
50 2
53 2
54 2
55 2
56 4
58 4
60 4
61 2
63 3
65 4
66 1
69 4
71 2
74 2
77 2
81 3
82 2
85 2
89 3
90 1
91 1
92 3
96 4


25

"""

forest = []
number_of_trees = int(input())
for i in range(number_of_trees):
    position, height = [int(j) for j in input().split()]
    forest.append((position, height))

cuts = 1
futhers_demolition_reach = forest[0][0] + forest[0][1]
for i in range(len(forest)-1):
    current_tree_reach = forest[i][0] + forest[i][1]

    #checking if previous tree could be so tall that reach futher than tree that's closer to next one
    futhers_demolition_reach = max (current_tree_reach, futhers_demolition_reach)

    #if next tree if too far, we need to cut the tree ourself
    if forest[i+1][0] >= futhers_demolition_reach:
        cuts += 1

print(cuts)