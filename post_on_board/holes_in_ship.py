"""
You are looking for holes in the hull of my boat. If there are at least one hole below sea level, then the boat will sink.

With your super-vision, you can see all the boat at once... but only in ASCII art. The water is always represented by ~ and the boat is outlined by \ and /. Holes are O, o or 0. But these icons can also represent non-hole objects when not inside a boat (like a fish for example), and a hole between brackets "{}" is a window!

Print the number of holes.
Input
Line 1 : Number N of line composing my boat.
N next lines : My boat
Output
X holes
Constraints
0 < N <= 30
Length of line <= 50
Example
Input

4
    |\  o
    | \-|______
~~~~~~~~\__o__/~~~~
~~~~~~~~~~~~~~~~~~~

Output

1

------------------------test2
4
  |\  o     o  /|
  | \-|_____|-/ |
~(O)~~\_____/~~(O)~
~^^^~~~~~~~~~~~^^^~

output
0
------------------------test3
 Motorboat

5
        __
  _____/_ | o
  \       |*|____--
~~~\__0_________o_/~~~
~~~~~~~~~~~~~~~~~~@@~~
output
2
------------------------test4
 People swimming

10
                  __
                 /||\
                / || \
               /  ||  \
              ----||----
             <|   ||
          ____|___||________
~~~~~~~~~|\                /~~~~~~~
~~>--o~~~|~\ O{o}    {o}  /~~~~~~~~
~~~~~~~~~|~~\o_____0___OO/~~~o--<~~
output
5
----------------------test5
1
~\_/~
output
0
----------------test6
30
                      __
                 ____ ||
         _______/    |||
        <____________\||
                      ||
                     /||--|\
                    / ||  (_^\
                   /v ||   ) .^
                  /^| ||   |   _\
                /^.^| ||   (_    ^
               /^- (  ||    |     ^\
              /^   |  ||    |      _\
             /_   _)  ||    |        ^
            /_    |   ||    |         ^\
           /_     |   ||    |          _\
          /_      (_  ||    |            ^
         /_        |  ||   _)             ^
        /.         |  ||   |               ^\
       /_          |  ||   |                ^\
      /_           (_ ||  _)                 _\
     /_             | ||  |                   _\
    /^     _________|-|| _)                     \
    ^_____/           ||-|______________________^
______                ||
\__   |_______________||_________________________
~~~\_        Oo0      ^^                      __/~
~~~~~\       {O}             {O}            _/~~~~
~~(O)~\_________________________________0___/~~~~~
~~^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

output 4

"""
import re

outerPattern = r'~\\.*[oO0].*/~'
innerPattern = r'(?=([^{][oO0][^}]))'

counter = 0
n = int(input())
for i in range(n):
    line = input()
    if result := re.search(outerPattern, line):
        print(result.group(0))
        counter += len(re.findall(innerPattern, result.group(0)))

print(counter)
