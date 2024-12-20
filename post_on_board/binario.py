'''
Validate that the given grid is a valid Binario.

Binario, also called Binary Sudoku, is a puzzle where you have to fill a nxn grid with 1s and 0s while satisfying these three guidelines :
1 - For each row and column, half the digits are 1s and the other half are 0s.
2 - For each row and column, there can never be more than two consecutive ones or two consecutive zeros.
3 - No two rows can be identical. No two columns can be identical.

If the grid is valid, output VALID.
If the grid is invalid, output the lowest index to an invalid row or, if all rows are valid, the lowest index to an invalid column. Indexes of rows and columns are zero-based.
Input
Line 1 : An integer n giving the size of the grid (n x n)
Next n lines : The n space separated digits for each row of the grid (starting with row 0)
Output
VALID if the grid is valid, else the lowest index to an invalid row or, if all rows are valid, the lowest index to an invalid column. Indexes of rows and columns are zero-based.
Constraints
6 ≤ n ≤ 14
n is always even.
The grid only contains 1s and 0s. There are neither empty cells nor other characters.
Example
Input

6
1 0 0 1 0 1
0 1 0 1 1 0
1 0 1 0 0 1
0 1 1 0 0 1
1 0 0 1 1 0
0 1 1 0 1 0

Output

VALID

-----------------test2
12
1 1 0 1 0 0 1 0 0 1 1 0
0 0 1 1 0 1 0 0 1 0 1 1
1 1 0 0 1 0 1 1 0 1 0 0
1 0 0 1 0 0 1 0 1 1 0 1
0 1 1 0 1 1 0 1 0 0 1 0
0 1 1 0 0 1 0 0 1 1 0 1
1 0 0 1 1 0 1 1 0 0 1 0
1 0 1 0 0 1 0 1 0 0 1 1
0 1 0 1 1 0 1 0 1 1 0 0
1 0 1 1 0 1 0 1 1 0 0 1
1 1 0 0 1 1 0 1 0 0 1 0
0 0 1 0 1 0 1 0 1 1 0 1
output
9
------------test3
8
1 1 0 0 1 1 0 0
1 0 0 1 0 0 1 1
0 0 1 0 1 1 0 1
1 1 0 1 0 0 1 0
0 0 1 1 0 1 1 0
0 1 0 0 1 0 1 1
1 1 1 0 1 0 0 0
0 0 1 1 0 1 0 1
output
6
-------------test4
10
1 0 0 1 1 0 1 1 0 0
0 1 1 0 0 1 1 0 0 1
1 0 1 0 0 1 0 1 1 0
0 1 0 1 1 0 0 1 0 1
0 1 1 0 1 0 1 0 1 0
1 0 0 1 0 1 0 0 1 1
1 0 0 1 1 0 1 1 0 0
0 1 1 0 0 1 0 0 1 1
1 0 1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1 0 1
output
6
--------------test5
12
1 0 1 0 0 1 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 0 1 0
0 0 1 1 0 1 1 0 0 1 0 1
0 1 1 0 1 0 0 1 0 1 0 1
1 0 0 1 1 0 0 1 1 0 1 0
0 1 1 0 0 1 1 0 1 0 1 0
1 1 0 0 1 0 1 0 0 1 0 1
0 0 1 1 0 1 0 1 1 0 1 0
1 0 0 1 0 0 1 1 0 1 0 1
0 1 1 0 1 1 0 0 1 0 1 0
1 0 0 1 0 1 0 1 1 0 0 1
0 1 0 1 1 0 1 1 0 1 0 0
output
7
---------------test6
12
1 1 0 0 1 0 0 1 1 0 1 0
1 0 1 1 0 0 1 0 0 1 0 1
0 0 1 1 0 1 0 1 1 0 1 0
1 1 0 0 1 0 1 0 1 0 1 0
0 0 1 1 0 1 0 1 0 1 0 1
0 1 0 0 1 1 0 1 1 0 0 1
1 0 0 1 1 0 1 0 0 1 1 0
0 1 1 0 1 0 1 0 1 0 0 1
0 1 0 1 0 1 0 1 0 1 0 1
1 0 1 0 0 1 1 0 0 1 1 0
1 1 0 0 1 0 0 1 1 0 0 1
0 0 1 1 0 1 1 0 0 1 1 0
4

'''

import itertools

the_list = []
the_set_length = 0
the_set = set()
rows_are_valid = True
n = int(input())
for i in range(n):
    the_list.append(input().replace(" ", ""))
    the_set.add(the_list[-1])
    the_set_length += 1
    print(the_list[-1])
    if not the_list[-1].count("1") == n // 2 or \
            any([1 if len(list(x[1])) > 2 else 0 for x in itertools.groupby(the_list[-1])]) or \
            not len(the_set) == the_set_length:
        print(i)
        rows_are_valid = False
        break

if rows_are_valid:
    the_set.clear()
    the_set_length = 0
    for i in range(n):
        temp = "".join([the_list[x][i] for x in range(n)])
        print(temp)
        the_set.add(temp)
        the_set_length += 1
        if not temp.count("1") == n // 2 or \
            any([1 if len(list(x[1])) > 2 else 0 for x in itertools.groupby(temp)]) or \
            not len(the_set) == the_set_length:
            print(i)
            break
    else:
        print("Valid")

