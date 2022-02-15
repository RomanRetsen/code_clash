'''Sum of two squares
def sum_of_two_squares(n):
Many positive integers can be expressed as a sum of exactly two squares of positive integers, both
possibly equal. For example, 74 = 49 + 25 = 7 2 + 5 2 . This function should ind and return a tuple of
two positive integers whose squares add up to n, or return None if the integer n cannot be so
expressed as a sum of two squares.
The returned tuple must present the larger of its two numbers irst. Furthermore, if some integer
can be expressed as a sum of two squares in several ways, return the breakdown that maximizes the
larger number. For example, the integer 85 allows two such representations 7 2 + 6 2 and 9 2 + 2 2 , of
which this function must therefore return (9, 2).
The technique of two pointers, as previously seen in the function two_summers in the
listproblems.py example program, directly works also on this problem! The two positions
start from both ends of the sequence, respectively, from where they inch towards each other in a
way that guarantees that neither can ever skip over a solution. This process must eventually come
to a de inite outcome, since one of the two things must eventually happen: either a working solution
is found, or the positions meet somewhere before ever inding a solution.
n Expected result
1 None
2 (1, 1)
50 (7, 1)
8 (2, 2)
11 None
123**2 + 456**2 (456, 123)
55555**2 + 66666**2 (77235, 39566)
(In binary search, one of these indices would jump halfway towards the other in every round,
causing the execution time to be logarithmic with respect to n. However, we are not in such a lucky
situation with this setup.)
'''
import math

def sum_of_two_squares(n):
    if n == 1:
        return None
    start = math.floor(n ** 0.5)
    for i in range(start, start//2, -1):
        end = n-i ** 2
        if (i ** 2 + math.floor(end ** 0.5) ** 2) == n:
            return (i, math.floor(end ** 0.5))
    else:
        return None

print(sum_of_two_squares(55555**2 + 66666**2))
print(sum_of_two_squares(123**2 + 456**2))
print(sum_of_two_squares(50))
print(sum_of_two_squares(85))
print(sum_of_two_squares(11))
print(sum_of_two_squares(1))
print(sum_of_two_squares(0))
print(sum_of_two_squares(74))
