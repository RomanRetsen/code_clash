'''
About division, the result need to be rounded up to the next integer.
Input
Line 1 : A string formula (always two numbers N and M, and one sign)
Output
formula's result as an integer
Constraints
0 ≤ N ≤ 9
0 ≤ M ≤ 9
Example
Input

3 + 6

Output

105


--------------------------
Subtraction

2 - 4

-2
-----------------------------


4 * 8

2912

---------------------------


5 / 0

2

---------------------------


0 + 0

96



'''

import math
import re

formula = input()
repl_func = lambda x:str(ord(x.group(0)))
f = re.sub(r"\d", repl_func, formula)
print((math.ceil(eval(f))))
