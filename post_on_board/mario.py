'''
A famous plumber is going through an ASCII adventure. He cannot jump, but mushrooms and flowers are still present.

- He has 4 different ordered states of power: Dead < Small < Tall < Overpowered
- Our hero always starts small.
- If he takes a mushroom M, he can go from small to tall. If a mushroom is taken when he is tall or overpowered, nothing happens.
- If he takes a flower F, he becomes overpowered whatever he was tall or small.
- Once dead, he cannot change his state

The only way to downgrade his state, is to be touched by a villain. He becomes tall if he was overpowered, small if he was tall and dies if he was small.
Villain can be of two types:
- Ground G, will always touch our hero
- Wings-equipped W, cannot touch our hero when he is small

"_" represent the ground, nothing happens on those characters

Return his state at the end of the level: Dead, Small, Tall or Overpowered
Input
length : Is the length of the map
map: describes the path
Output
Return his state at the end of the level: Dead, Small, Tall or Overpowered
Constraints
5 < length < 100
map only contains M,F,G,W or _
Example
Input

12
___M____G___

Output

Small
----------------test2
9
____G____
output
Dead
--------------test3
9
____W____
output
Small
--------------test4
14
___M___G___M__
output
Tall
---------------test5
12
__F__W__W_W_
output
Small
--------------test6
60
_____W___W____M__W___F__GG_W_M___G___W___G__M__W_W__F__G__G_
output
Dead
----------------test7
29
__FGG_W__W__M__W__F_G__F__M__
output
Overpowered
'''

import sys
import math

state = "Small"
all_states = {"Small": {"down": "Dead", "up": "Tall"}, "Tall": {"down": "Small", "up": "Overpowered"}, "Overpowered": {"down": "Tall", "up": "Overpowered"}}
length = int(input())
_map = input()


def downgrade(x):
    return all_states[x]["down"]


def upgrade(x):
    return all_states[x]["up"]


for step in _map:
    if step == "G":
        if (state := downgrade(state)) == "Dead":
            break
    elif step == "W" and not state == "Small":
        state = downgrade(state)
    elif step == "M":
        if state == "Small":
            state = "Tall"
    elif step == "F":
        state = "Overpowered"
print(state)

