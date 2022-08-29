'''
Find the closest product of 2 prime numbers.

input
A single integer n.
Output
A single line containing the closest prime product to the given integer n.
Constraints
2 ≤ n ≤ 200
There will always be only 1 possible solution
Example
Input

23

Output

22
------------
35

35
------------

28

26
------------

2

4
-------------


189

187

'''
def is_prime(n):
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
    return True

def is_good(input):
    start = 2
    end = (input // 2) + 1
    while start < end:
        if input % start == 0 and is_prime(start) and is_prime(input // start):
            return True
        start += 1
    return False

distance = 0
result = 0
n = int(input())
while True:
    print(f"Trying {distance}")
    if (n - distance) > 1 and is_good(n - distance):
        result = n - distance
        break
    elif is_good(n + distance):
        result = n + distance
        break
    distance += 1

print(result)
