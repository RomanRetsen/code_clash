"""
Convert the number from binary to decimal
0 can be "false", "no", "zero", or "0"
1 can be "true", "yes", "one", or "1"
Most significant bit is on the left
Input
Ligne 1 : All binary digits on the same line, each represented by a word, separated by a space
Output
The unsigned integer value N
Constraints
No more than 30 bits
Example
Input

1 0 yes no one true yes false yes zero 1 0 1

Output

5589

---------------test2
zero 0 false true no 1 false

output
10
---------------test3
true true true true

output
15
--------------test4
One 1 one one 1 one one true one one one one one 1 true one one one one true one one 1 one true 1 one 1 one one

output
1073741823
"""

import sys
import math

posibility = {"false":0, "no":0, "zero":0, "0":0, "true":1, "yes":1, "one":1, "1":1}
binary = int("".join([str(posibility[x.lower()]) if x.lower() in posibility.keys() else "" for x in input().split()]), 2)


print(binary)