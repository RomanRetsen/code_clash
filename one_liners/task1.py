'''
Given n print sum of cubes from 1 to i where 1<=i<=n on each i line.
Input
Line 1:An integer n
Output
n Lines: Sum of cubes
Constraints
0<n<50
Example
Input

2

Output

1
9
-------------------
input 
3
output
1
9
36
-------------------
input
25
output
1
9
36
100
225
441
784
1296
2025
3025
4356
6084
8281
11025
14400
18496
23409
29241
36100
44100
53361
64009
76176
90000
105625
'''
import itertools
n = int(input())
print(*list(itertools.accumulate(range(1, n + 1), func=lambda x,y:x+y**3)), sep="\n")