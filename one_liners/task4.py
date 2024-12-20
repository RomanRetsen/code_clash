'''
A cipher is an algorithm used to encrypt/encode a message. Here is a simple one. The letters in the message will be "encoded" by a shift up or down the alphabet. Case will be preserved. If a shift goes past the end of the alphabet, it will wrap around back to the beginning and vice versa.
Input
Line 1: An integer n for the cipher shift number.
Line 2: A character d shift direction left < or right >.
Line 3: A string m message to encode/decode, consisting of only characters a-z, A-Z, or space.
Output
Line 1: The new encoded/decoded message. Alphabet characters will be encoded, while space will be ignored. Case will be preserved.
Constraints
0 ≤ N ≤ 26
d is either < or >
Example
Input

1
>
Gdkkn Vnqkc

Output

Hello World

------------------test 2
input
3
>
ABCD efgh

output
DEFG hijk
------------------test3


5
<
Ny bfx fqq f iwjfr

output
It was all a dream
-----------------------test 4


10
<
The Quick brOwn fOx

output
Jxu Gkysa rhEmd vEn



'''

import string
import collections

lower_c = collections.deque(string.ascii_lowercase)
upper_c = collections.deque(string.ascii_uppercase)

n = int(input())
d = input()
m = input()

if d == ">":
    lower_c.rotate(n)
    upper_c.rotate(n)
elif d == "<":
    lower_c.rotate(-n)
    upper_c.rotate(-n)

print(*[string.ascii_lowercase[lower_c.index(x)] \
        if x in string.ascii_lowercase else \
        string.ascii_uppercase[upper_c.index(x)] \
        if x in string.ascii_uppercase else \
        x for x in m], sep="")