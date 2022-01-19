'''
You are given two words. Find the first matching character between the two words in respect to the first word, and then output the one with the largest length of the two horizontally and the smallest length vertically (if both words are of the same length then the second word given should be placed horizontally).

Both outputs have to separate each character with a space and be all uppercase, all while making a crossword from the two words.

If the two words given do not having a matching character, then output:

NO COMMON CHARACTER

Input
Line 1: A string, words, separated by a space representing the words in order.
Output
The crossword from the two words
or

NO COMMON CHARACTER

Constraints
1 ≤ words length ≤ 14
Example
Input

cinnamon apple

Output

C I N N A M O N
        P
        P
        L
        E

-----------------test2
zz zz
output
Z Z
Z
------------------test3
too fox
output
  T
F O X
  O
  ---------------test4
  big nate
  output
  NO COMMON CHARACTER
  ---------------------test5
  willis college

  output

    W
    I
C O L L E G E
    L
    I
    S
'''

def print_cross(w1, w2, index1, index2):
    w1l = len(w1)
    w2l = len(w2)
    if w1l > w2l:
        for i in range(index2):
            print(w2[i].upper().rjust(index1 * 2 + 1, " "))
        print(*word1.upper())
        for i in range(index2+1, w2l):
            print(w2[i].upper().rjust(index1 * 2 + 1, " "))
    else:
        for i in range(index1):
            print(w1[i].upper().rjust(index2 * 2 + 1, " "))
        print(*word2.upper())
        for i in range(index1+1, w1l):
            print(w1[i].upper().rjust(index2 * 2 + 1, " "))

word1, word2 = input().split()

if len(set(word1).intersection(set(word2))) == 0:
    print("NO COMMON CHARACTER")
else:
    for index1, char in enumerate(word1):
        if not (index2 := word2.find(char)) == -1:
            print_cross(word1, word2, index1, index2)
            break # only first chars intersection is needed


