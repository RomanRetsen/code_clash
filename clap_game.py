"""
Clap@7 is a game played by a group of people, whereby each person will call out numbers, in ascending order, starting from 1. However, if the number satisfies any of the following conditions:

> The number is divisible by 7
> The number has the digit 7 in it
> The sum of the digits of the number is divisible by 7

Then the person has to clap instead of calling out the number. If the person does not perform the correct action, he loses.

Given an integer N, determine how many claps there have been, if the game has terminated at N, including N.

An example is shown, where three players A, B and C are playing this game.

A: 1
B: 2
C: 3
A: 4
B: 5
C: 6
A: CLAP
B: 8
C: 9
A: 10
B: 11
C: 12
A: 13
B: CLAP
C: 15
A: CLAP
B: CLAP
C: 18
Input
Line 1: An integer N which is the number at which the game has ended.
Output
Print the number of CLAPS
Constraints
1 ≤ N ≤ 3000000
Example
Input

17

Output

4

------------test2

80

33

-----------test3

236

92

----------teset4

3000000

1828649

------------test5

1

0

_____________
"""
def to_clap_or_not_to_clap(n):
    if n % 7 == 0:
        return True
    temp = 0
    while n // 10 > 0:
        cycle_temp = n % 10
        if cycle_temp == 7:
            return True
        temp += cycle_temp
        n //= 10
    if n == 7:
        return True
    temp += n
    if temp % 7 == 0:
        return True
    return False

n = int(input())
counter = 0
for i in range(1, n + 1):
    if to_clap_or_not_to_clap(i):
        counter += 1

print(counter)

