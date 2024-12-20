"""
A natural number is said to be a Narcissistic Number if the sum of its digits each raised to the power of the total number of digits is equal to that number.

eg. 153 = 1^3 + 5^3 + 3^3 = 153
Hence , 153 is a Narcissistic Number.
Input
Line 1: A natural number N
Output
Line 1: 'true' if N is a narcissistic number else output 'false'
Constraints
0<N
Example
Input

153

Output

true

-------test2

372

false

--------test3

548834

true

----------test4

32164049751

false


"""

def num_len(n):
    temp = 1
    while n // 10 > 0:
        temp += 1
        n //= 10
    return temp

def is_nar(n):
    original_n = n
    nl = num_len(n)
    #nl = len(str(n).lstrip("-"))
    temp = 0
    while n // 10 > 0:
        temp += (n % 10) ** nl
        n //=10
    temp += n ** nl
    # print(temp)
    if temp == original_n:
        return True
    else:
        return False

num = int(input())

if is_nar(num):
    print("true")
else:
    print("false")
