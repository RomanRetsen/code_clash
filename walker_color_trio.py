'''
COLOR TRIO

def colour_trio(colours):
This problem was inspired by the Mathologer video “Secret of Row 10”. To start, assume the
existence of three values called “red”, “yellow” and “blue”. These names serve as colourful (heh)
mnemonics and could as well have been 0, 1, and 2, or “foo”, “bar” and “baz”; no connection to actual
physical colours is implied. Next, de ine a rule to mix such colours so that mixing any colour with
itself gives that same colour, whereas mixing any two different colours always gives the third colour.
For example, mixing blue to blue gives that same blue, whereas mixing blue to yellow gives red,
same as mixing yellow to blue, or red to red.
Given the irst row of colours as a string of lowercase letters, this function should construct the
rows below the irst row one row at the time according to the following discipline. Each row is one
element shorter than the previous row. The i:th element of each row comes from mixing the colours
in positions i and i + 1 of the previous row. Rinse and repeat until only the singleton element of the
bottom row remains, returned as the inal answer. For example, starting from the irst row
'rybyr' leads to 'brrb', which leads to 'yry', which leads to 'bb', which leads to 'b' for the
inal answer, Regis. When the Python virtual machine laughingly goes 'brrrrr', that will lead to
'yrrrr', 'brrr' , 'yrr', and 'br' for the inal answer 'y' for “Yes, please!”
colours Expected result
'y' 'y'
'bb' 'b'
'rybyry' 'r'
'brybbr' 'r'
'rbyryrrbyrbb' 'y'
'yrbbbbryyrybb' 'b'
(Today's ive-dollar power word to astonish your friends and coworkers is "quasigroup".)
'''

color = input()
mixin = {frozenset("ry"):"b", frozenset("by"):"r", frozenset("br"):"y",
         frozenset("y"):"b", frozenset("b"):"b", frozenset("r"):"r",
         frozenset("yy"):"y", frozenset("bb"):"b", frozenset("rr"):"r",
         }
new_color = []
while len(color) > 1:
    for i in range(0, len(color)-1):
        new_color.append(mixin[frozenset(color[i:i+2])])
    color = "".join(new_color)
    new_color.clear()
else:
    print(color)

