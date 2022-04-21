'''
Consider a lemonade shop that sells bottles of lemonade. You can buy 1 bottle of lemonade with 1 coin. 3 empty bottles can be exchanged for 1 full bottle of lemonade. You can borrow (any number of) empty bottles from the shop if necessary, but you need to give them back at the end.

Given the number of coins you have at the start, how many bottles of lemonade can you drink at most?

E.g.
Input: 1
Output: 1
You have 1 coin, and buy 1 bottle of lemonade.

Input: 2
Output: 3
You have 2 coins. After drinking 2 bottles of lemonade, you can borrow 1 empty bottle, exchange them for 1 full bottle of lemonade, then give the empty bottle back.
Input
An integer c represents the number of coins you have.
Output
An integer b represents the number of bottles of lemonade you can drink.
Constraints
1≤c≤1000
Example
Input

1

Output

1

-------------test 2
2
output
3
-------------test3
3
output
4

-----------------test 4
4
output
6
-----------test5
999
output
1498
--------test6
142
output
213

'''
import sys
import math

c = int(input())
counter = empty = c

while empty > 2:
    print(f"empty: {empty}")
    a,b = divmod(empty, 3)
    counter += a
    empty = a + b
else:
    if empty == 2:
        counter += 1
print(counter)

print(f"Other simple solution {c * 3 >> 1}")