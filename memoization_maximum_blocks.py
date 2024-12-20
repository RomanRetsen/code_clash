"""
I want to construct a tower of height H by stacking blocks in a straight line going upwards.

However I only have two types of blocks: blocks of height P and blocks of height Q, with P ≤ Q.

If any combination of these two types of blocks is allowed, what is the maximum amount of blocks that can be used to construct the tower?

If it is impossible to construct the tower, the output should be 0.
Input
Line 1: One integer H, the desired height of the tower.
Line 2: Two space-separated integers P and Q, the heights of the available blocks.
Output
Line 1: Maximum amount of blocks required, or 0 if impossible to construct.
Constraints
1 ≤ H ≤ 1000

1 ≤ P ≤ Q ≤ 1000
Example
Input

10
3 4

Output

3



12
3 4

4
_________________

11
4 5

0


____________________

257
3 7

83

________________________
999
1 1000

999
_________________________


25
25 26

1
_____________

999
2 4

0

_______________


"""



#using memoization methond.

n = int(input())  # Desired height of the tower.

blocks_list = [int(i) for i in input().split()]

all_heights = [0 for _ in range(n + 1)]
for block in blocks_list:
    if block <= n:
        all_heights[block] = 1

for i in range(1, n + 1):
    for block in blocks_list:
        if block <= i:
            sub_res = all_heights[i - block]
            if sub_res + 1 > all_heights[i] and sub_res != 0:
                all_heights[i] = sub_res + 1

if all_heights[n] == 0:
    print(0)
else:
    print(all_heights[n])

