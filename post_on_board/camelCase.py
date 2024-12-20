"""

Input
First line: a string S containing one or many words.
Second line: one integer N specifying how many lowercase letters you have to left between uppercase letters.
Output
A unique line with the string S converted in Pseudo Camel Case.
Constraints
0 ≤ N ≤ 255
S contains only letters or spaces.
Example
Input

CamelCase
2

Output

CamElcAse
--------------test2
Up me if you can
3
output
UpmeIfyoUcan

-----------------test3
The quick brown fox jumps over the lazy dog
4
ThequIckbrOwnfoXjumpSoverThelaZydog

---------------test4
Jackdaws love my big sphinx of quartz
0
output
JACKDAWSLOVEMYBIGSPHINXOFQUARTZ

-------------test5
To be or not to be that is the question
255
output
Tobeornottobethatisthequestion

---------------test6
A horse a horse my kingdom for a horse
1
output
AhOrSeAhOrSeMyKiNgDoMfOrAhOrSe
1
"""

s = input().replace(' ', '').capitalize()
n = int(input()) + 1
print("".join([x.upper() if index % n == 0 else x for index,x in enumerate(s)]))
