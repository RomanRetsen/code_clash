"""
You are given a pattern repeated in string S, and you have to print the smallest possible pattern one time, example:

if S = ABCABCABCABC, you print ABC
Input
String S, a pattern repeated, with no spaces
Output
the pattern unrepeated
Constraints
The pattern S will repeat itself at least 2 times.
Example
Input

CodingCoding

Output

Coding
----------test2
AAAAAAAAAAAAAAAA

output
A
-----------test3
25352535

output
2535
------------test4
AB34EAB34EAB34EAB34E

ouput
AB34E
-----------test5
egaugnalnoiegaugnalnoiegaugnalnoiegaugnalnoiegaugnalnoiegaugnalnoiegaugnalnoiegaugnalnoi

ouput
egaugnalnoi
----------test6
AbcdAbcdAbcd3AbcdAbcdAbcd4AbcdAbcdAbcd5AbcdAbcdAbcd3AbcdAbcdAbcd4AbcdAbcdAbcd5
AbcdAbcdAbcd3AbcdAbcdAbcd4AbcdAbcdAbcd5
-----------test7

1212112121121211212112121

output
12121
"""




import math

s = input()
the_index = 0
for indx, c in enumerate(s[1:]):
    l = indx + 1
    if s[indx+1:].count(s[:indx+1]) == math.ceil((len(s[indx+1:]) / len(s[:indx+1]))):
        the_index = indx
        break

print(s[:the_index + 1])