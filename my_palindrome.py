import string

letters = {x:0 for x in string.ascii_lowercase}

s = input()
for i in s:
    letters[i] += 1

print(sorted([x for x in letters.items() if x[1] > 0], key=lambda x:x[0]))

center_element = ''
final = []
for i in sorted([x for x in letters.items() if x[1] > 0], key=lambda x:x[0]):
    if i[1]%2 == 1 and not center_element:
        center_element = i[0]
    final.append(i[0] * (i[1] // 2))
print(*[ x for x in final if x],center_element,*[x for x in final[::-1] if x ], sep="" )

# 23
# michaeljacksonandzzorro
#
# result
# acnorzazronca
#
# You are given an integer L and a string S of L letters (lower case), without space. Your objective is to take some of these letters, put them in any order you want, and build a palindrome with the maximum possible length. And among all possible longest palindromes, output the one which is the smallest in lexicographic order.
# Input
# Line 1: the length L of the string
# Line 2: the string S of L lower case letters, without spaces.
# Output
# A string of lower cases representing the palindrome made of letters from S and having the maximum length possible but being the smallest in lexicographic order (among all maximum length palindromes)
# Constraints
# 1 < L < 1000
# Example
# Input
#
# 8
# bbaabbaa
#
# Output
#
# aabbbbaa
#
