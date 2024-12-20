"""
A bouncy number is a positive integer that, when read from left to right, is neither only increasing nor only decreasing. For example, 12341 is bouncy, while 12345 and 54321 are not bouncy.

Your program must determine if a given input number is bouncy.
Input
Line 1 A non-negative integer N
Output
A single line containing true if N is bouncy, and false otherwise.
Constraints
0 ≤ N ≤ 10^10
Try solving the task without using conversion to string but use math only


Example
Input

12341

Output

true

--------test 2

1122334455

false


--------test 3
977543

false

------test 4

0

 false

 --------test 5

 915544332

true
"""

n = int(input())

up = False
down = False
current = n % 10
while n // 10 > 0:
    n = n // 10
    if n % 10 > current:
        up = True
        current = n % 10
    elif n % 10 < current:
        down = True
        current = n % 10

if up and down :
    print("true")
else:
    print("false")