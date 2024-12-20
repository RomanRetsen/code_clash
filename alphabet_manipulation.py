"""
Print n letters of the alphabet in order and starting from the letter s. Letter case should be the same as letter s. Wrap back to the start of the alphabet after 'z' or 'Z'.
Input
Line 1: An integer n for the number of letters to print.
Line 2: The starting letter s.
Output
An alphabet string n letters long starting from letter s, in the same case as s.
Constraints
1 ≤ n ≤ 100
s is a character (lower or upper case)
Example
Input

3
a

Output

abc

--------test2

4
z

zabc

-------test3

2
J

JK

_---------test4

27
b

bcdefghijklmnopqrstuvwxyzab

------------test5

100
A

ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUV

-------------test6

1
h

h

----------------
"""


n = int(input())
s = input()
start_point = ord(s) - 65 if s.isupper() else ord(s) - 97
correction = 65 if s.isupper() else 97
for i in range (n):
    print(chr((start_point + i) % 26 + correction), end='')



#other guy's approach

# a='abcdefghijklmnopqrstuvwxyz'
# n = int(input())
# s=input()
# start=a.find(s.lower())
#
# for i in range(n):
#     if s.islower():
#         print(a[(start+i)%26],end='')
#     else:
#         print(a[(start+i)%26].upper(),end='')
