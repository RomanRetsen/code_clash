"""
 Given a list of values for "teeth" in a key, determine the arithmetic operations and final result based on the following rule set:

Compare the first two values, then compare the result with the third, and so on.

Example key(read left to right) 1 7 2 5 <-- value A would be 1, value B would be 7

- If A is greater than B, SUBTRACT
- if B is greater than or equal A, ADD, but only if both values are odd, or both are even. Otherwise MULTIPLY
- if at ANY time B is a divisor of A, DIVIDE

- A pin is never valued at 0
- At no time will the result of an equation be 1 or 0

Example:
1 7 2 5 <-- 1 and 7 are compared and added to make 8
8 and 2 are compared and divided to make 4
4 and 5 are compared and multiplied, and the final result is 20
Input
- A single integer n stating the number of pins
- A string x listing each pin value, space separated

Example Input:
4
1 7 2 3
Output
A single line listing the arithmetic operators used to the final result, followed by the final result, space separated

Example Output:
+/- 20
Constraints
4<=N<=10
0<Pin Value<10
Example
Input

4
1 5 9 4

Output

+*- 50

-------------test2

6
1 2 3 4 5 6

**-*- 4

-------------test3
8
1 9 4 5 8 3 7 6

+--*-+/ 2

------------test4

10
2 4 5 5 9 2 3 6 9 3


+-+*//-+/ 4
"""

#return tuple of type of operation performed and result of operation
def oper(x, y):
    if x % y == 0 and x > y:
        return ("/", x//y)
    elif x > y:
        return ("-",x-y)
    elif ( x % 2 == 0 and y % 2 == 0 ) or (x % 2 == 1 and y % 2 ==1):
        return ("+", x + y)
    else:
        return ("*", x * y)

n = int(input())
x = [int(x) for x in input().split()]
r = []
temp = x[0]
for i in range(1,len(x),1):
    result = oper(temp, x[i])
    r.append(result[0])
    temp = result[1]

print("".join(r), temp)
