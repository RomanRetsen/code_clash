'''

Input
Line 1: A number representing the max amount of money you have
Line 2: A comma delimited string of your shopping list
Line 3: Number of items available for purchase
Next 'N' Lines: An Item and its price separated by a comma
Output
A string true/false for whether you can purchase or not.
If you Can Purchase (true), output the money remaining afterwards.
If you Cannot Purchase (false), output how much more money you would need to be able to purchase everything on the list.
Constraints
Max amount of money > 0
Shopping List has at least 1 item
N > 0
All prices in whole dollars
Example
Input

2
Lemonade
1
Lemonade,2

Output

true
0
--------------test 2


10
Gum,Chips,Soda
4
Chips,2
Ice Cream,5
Gum,1
Soda,3

output
true
4
--------------test3


40
Bread,Apples,Black Forest Ham,Mayonnaise,Lettuce,Bacon
10
Cereal,7
Bread,5
Bacon,10
Apples,10
Mayonnaise,10
Tomato,6
Milk,4
Chips,5
Black Forest Ham,6
Lettuce,8

output
false
9
-----------test4


2500
Gaming Computer,Monitor,Mouse,Keyboard,Headset
9
Laptop,800
Mouse,50
Keyboard,75
Gaming Computer,1800
Headset,100
Speakers,250
iPhone,800
Monitor,350
Android Phone,500

true
125





'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_max = int(input())
s_list = input()
n = int(input())
store = {}
for i in range(n):
    _str = input().split(",")
    store[_str[0]] = int(_str[1])

fail = False
for i in s_list.split(","):
    if not store[i] or not store[i] <= _max:
        fail = True
    _max -= store[i]
else:
    if fail:
        print("false")
        print(_max * -1)
    else:
        print("true")
        print(_max)

'''
# smart people solution
m=int(input())
l=input().split(',')
s=0
for i in [0]*int(input()):
 i,p=input().split(',')
 if i in l:s+=int(p)
print([f"true\n{m-s}",f"false\n{s-m}"][s>m])
'''

