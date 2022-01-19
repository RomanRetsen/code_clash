"""

 Goal
Your task is to invert a given text t. For characters the alphabet is turned around like this:

a = z
b = y
c = x
...
x = c
y = b
z = a

Cases of letters are not affected in the inversion: A = Z, B = Y ...


Numbers are changed like this:

0 = 9
1 = 8
...
8 = 1
9 = 0

Brackets ((), [], {}) are turned around like this:

[ = ]
( = )
{ = }
] = [
) = (
} = {

Spaces and punctuation are not changed.
Input
Line 1: The text t.
Output
Line 1: The inverted text t
Constraints
1 ≤ Length of t ≤ 150
Example
Input

ab

Output

zy

----------test2
ab
output
zy

-----------------test3
.,? and ! are also important.
output
.,? zmw ! ziv zohl rnkligzmg.

-----------------test4
I hope, your program succeeded in Testcase 1, 2, 3, 4 and 5. Then you will probably get 100%.

output
R slkv, blfi kiltizn hfxxvvwvw rm Gvhgxzhv 8, 7, 6, 5 zmw 4. Gsvm blf droo kilyzyob tvg 899%.

-----------------test5
5 * 8 - 98 + 34 = -24
output
4 * 1 - 01 + 65 = -75

-----------------test6
This is a Testcase to find out, if your program turns brackets (like (, ), [, ], { and }) around.

output
Gsrh rh z Gvhgxzhv gl urmw lfg, ru blfi kiltizn gfimh yizxpvgh )orpv ), (, ], [, } zmw {( zilfmw.

--------------------test7
print({"1":"You entered 1.", "2":"You entered 2"}[input()])

ouput
kirmg)}"8":"Blf vmgvivw 8.", "7":"Blf vmgvivw 7"{]rmkfg)([(

"""
import string

my_dict = {x:chr(ord(x)-) for x in string.ascii_letters}
t = input()

for i in range(len(t)):
    print(chr(ord(t[i]) + 32), end="")
