"""
A narcissistic number is a number that equals the sum of its own digits each raised to the power of the number of digits.
For example, 153 is a narcissistic number because 1^3 + 5^3 + 3^3 = 153.
The first few narcissistic numbers are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, and 371.

Find the amount of narcissistic numbers between 2 given integers m and n (excluding m and n).

Example:
m=0 and n=99
The narcissistic numbers in this range are 1,2,3,4,5,6,7,8,9, so the answer is 9.
Input
Line 1: 1 integer, m
Line 2: 1 integer, n
Output
Line 1: An integer a, counting the amount of narcissistic numbers between m and n.
Constraints
-1<m<1000
m<n<100000
Example
Input

0
99

Output

9



--------------test2

-1
1000

14

-------------test3
10
10000

7

------------test4

0
100000

19
-------------test5

105
1991

5

-------------test6
571
47999

3

-------------test 7
50
10000


7


"""
def is_nar(n):
    compare__n = n
    l = len(str(n).lstrip("-"))
    temp = 0
    while n // 10 > 0:
        temp += (n % 10) ** l
        n //=10
    temp += n ** l

    if temp == compare__n:
        return True
    else:
        return False

m = int(input())
n = int(input())

c = 0
for i in range(m + 1, n, 1):
    if is_nar(i):
        c += 1

print(c)


