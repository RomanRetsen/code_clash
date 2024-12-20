'''
You work at McBurger's and are responsible for cooking burgers. McBurger has N ingredients available.
On your shelf, you receive P burger orders.
Your job is to find out whether it is possible to design all the orders with the N ingredients you have. You will have to report back to Bob, your chef, and tell him if you have enough ingredients to make everything.
Input
Line 1: N available ingredients.
Line 2: A list of N ingredients represented by an uppercase and separated by a space.
Line 3: P orders.
Following P lines: An order, with the necessary ingredients separated by a space.
Output
Line 1: YES if you can do all the orders, else NO.
Constraints
1 ≤ N ≤ 50
1 ≤ P ≤ 10
1 ≤ maximum length of an order ≤ 40
Example
Input

5
S S M M P
2
P M
S S

Output

YES



------------------------


1
C
1
P C M

NO


-------------------------


26
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
1
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

YES

---------------------------


50
A B Z A B C D E O P Q R S T U V W X F G H I J C D E F G H I J K L M N O P Q R S T U V W X Y K L M N
10
A B
Z A Z
F C D
F D D R
P M 
L O P A Z
L O R A C X
Z A C
G C D G C D L C M
H

NO

'''

import sys
import math
from collections import Counter

n = int(input())
ingre = input()
we_have = Counter(ingre)
p = int(input())
chance = 1
for i in range(p):
    order = input().split()
    for part in order:
        if not part in ingre or we_have[part] == 0:
            print("NO")
            chance = 0
            break
        else:
            we_have[part] -= 1
    if not chance:
        break
else:
    print("YES")
