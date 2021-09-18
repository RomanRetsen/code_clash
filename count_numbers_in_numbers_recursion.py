#version 3

#version 1
def count_in_list2(c, s_list):
    counter = 0
    for e in s_list:
        for a in str(c):
            if int(a) == e:
                counter += 1
    return counter

#version 2

def count_in_number(c, element):
    counter = 0
    if c // 10 == 0 and c % 10 == element:
        return 1
    elif c//10 > 0 and c%10 == element:
        counter += 1
        counter += count_in_number(c // 10, element)
    elif c//10 >0 and not c%10 == element:
        counter += count_in_number(c // 10, element)
    return counter


def count_in_list(c, s_list):
    counter = 0
    for element in s_list:
        counter += count_in_number(c, element)

    return counter


v = int(input())
n = int(input())
selection_list = []
total_in_sublist = 0
total_all_numbers = 0

for i in input().split():
    selection_list.append(int(i))

for i in range(v):
    cycle_number =  count_in_list(i, selection_list)
    if cycle_number > 0:
        total_in_sublist += 1
        total_all_numbers += cycle_number

print(total_in_sublist, total_all_numbers, sep="\n")




# Given a number v and a set of digits d.
# In the range of numbers from 0 up to but not including v:
# 1) Count the numbers that have any of the digits d in their decimal representation.
# 2) Count the total number of occurrences of all the digits d in the decimal representations of the numbers. ex: 1999 contains three 9s.
#
# Example: with d= [1, 2]
# v=15 => [0 1 2 3 5 6 7 8 9 10 11 12 13 14]
# 1) The first number counts the numbers containing 1 or 2:
# numbers that contain 1 or 2 = [1, 2, 10, 11, 12, 13, 14] => 7
# 2) The second number is the total number of 1s and 2s:
# numbers that contain digit 1 or 2 = [1, 2, 10, 11, 12, 13, 14]
# => number of 1s and 2s in each = [1, 1, 1, 2, 2, 1, 1] => 9
# Input
# Line 1: v
# Line 2: n
# Line 2: n space separated values d
# Output
# Line 1: The count of numbers that have any digit from d
# Line 2: The total number of the digits d
# Constraints
# 0 ≤ v ≤ 10000
# 1 ≤ n ≤ 10
# Each value in d is a single digit 0-9
# No repeating values in d
# Example
# Input
#
# 10
# 1
# 9
#
# Output
#
# 1
# 1
#
#
#
#
# 100
# 1
# 9
#
#
# 19
# 20
# ____________
#
# 100
# 2
# 8 9
#
# 36
# 40
#
# _________
#
# 95
# 1
# 9
#
# 14
# 14
#
# ____________
# 10000
# 1
# 9
#
#
# 3439
# 4000
#
#
# ____________
#
#
# 1000000
# 1
# 9