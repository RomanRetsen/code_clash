"""
Given two sentences, s_1 and s_2, return whether they are shadows of each other.
This means that all of the word lengths are the same and words in corresponding positions don't share any common letters whatsoever.
If shadow sentences: print shadow

else print the reason that they are not shadows (check in the order provided):

not the same amount of words in both strings
some of the corresponding words not the same length
shared letters in corresponding words
Input
Line 1: s_1
Line 2: s_2
Output
shadow or one of the reasons that the strings are not shadows
lengths of the words, space-separated for the 2 strings in order
Constraints
length(s_1), length(s_2) < 30
the two strings will only have lowercase letters
Example
Input

they are round
fold two times

Output

shadow

----------test2

seemingly unlimited
cutthroat crossbows

output

shadow
-----------test3
own a boat
buy my wine

output

some of the corresponding words not the same length

------------test4
a normal sentence
a normal sentence

output

shared letters in corresponding words

----------test5
this is a quote
so is this

output

not the same amount of words in both strings
"""

s_1 = input().split()
s_2 = input().split()
l = len(s_1)
e = False
if len(s_1) == len(s_2):
    if "".join([str(len(x)) for x in s_1]) == "".join([str(len(x)) for x in s_2]):
        for i in range(l):
            ll = len(s_1[i])
            for y in range(ll):
                if s_1[i][y] == s_2[i][y]:
                    e = True
                    break
            if e:
                print("shared letters in corresponding words")
                break
        else:
            print("shadow")
    else:
        print("some of the corresponding words not the same length")
else:
    print("not the same amount of words in both strings")
