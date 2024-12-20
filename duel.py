"""
The program:
Two adventurers are going to duel, each of them has health points HP1 and HP2 and apply D1 and D2 damage at their opponents each round.

Your program must output which adventurer win and how many round are needed to end the duel.
There are no draw.

INPUT:
Line 1: Health point HP1 and damage D1 of the first duelist.
Line 2: Health point HP2 and damage D2 of the second duelist.

OUTPUT:
Line 1: The winner number 1 or 2 and how many rounds were needed to end the duel.

CONSTRAINTS:
0 < HP1 ≤ 10000
0 < HP2 ≤ 10000
0 ≤ D1 ≤ 50
0 ≤ D2 ≤ 50

EXAMPLE:
Input
100 1
2 1
Output
1 2

----------test2 

6789 42
9876 20

1 236

-------------test3 tricky

10 4
1337 0


1 335

-----------test4

1 1
9001 9001


2 1


"""

import math

hp1, d1 = [int(i) for i in input().split()]
hp2, d2 = [int(i) for i in input().split()]
strike_needed1_die = (2, math.inf) if d2 == 0 else (2, math.ceil(hp1 / d2))
strike_needed2_die = (1, math.inf) if d1 == 0 else  (1, math.ceil(hp2 / d1))

win_number, win_cycles = min((strike_needed1_die, strike_needed2_die), key=lambda x:x[1])
print(win_number, win_cycles)
