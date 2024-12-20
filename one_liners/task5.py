'''
Line 1 : One string separate by space with x1 and y1 for the coordinates of Gobball, x2 and y2 for the coordinates of Evangelyne, rng and mp for the characteristics of Evangelyne.

rng (range) is the distance of Evangelyne can shoot an arrow.
mp (speed) is the distance of Evangelyne can move in one turn.
Output
Line 1: The number of turns it takes Evangelyne to kill Gobball, or FIGHT NOW.
Constraints
x1,x2,y1,y2,rng,mp are all integers
0 <= x1,x2,y1,y2 <=100
0 < rng <= 10
0 < mp <= 6
Example
Input

12 87 0 10 4 5

Output

17
-------------test2


0 0 0 0 3 6

FIGHT NOW

---------------test 3


2 14 15 20 4 3

5

----------------test 4


8 53 23 2 8 4

15

--------------test 5


18 8 6 10 2 6

2



'''
'''

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x_1, y_1, x_2, y_2, rng, mp = [int(i) for i in input().split()]
counter = 1
current_mp = mp
while True:
    print(x_1, y_1, x_2, y_2, f"counter {counter}")
    if ((x_1 - x_2) ** 2 + (y_1 - y_2)**2) ** 0.5 <= rng:
        if counter <= 1:
            print("FIGHT NOW")
            break
        else:
            counter += 1
            print(counter)
            break
    else:
        if abs(x_1 - x_2) > abs(y_1 - y_2):
            if x_2 > x_1:
                x_1 += 1
            else:
                x_1 -= 1
        else:
            if y_2 > y_1:
                y_1 += 1
            else:
                y_1 -= 1
        if current_mp == 1:
            counter += 1
            current_mp = mp
        else:
            current_mp -= 1
'''
print(bytes('ⱸⱹⱘⱙⱏ⁍椽灮瑵⤨献汰瑩⤨琊愽獢椨瑮砨⴩湩⡴⥘⬩扡⡳湩⡴⥙椭瑮礨⤩椭瑮伨਩㵳湩⡴⽴湩⡴⥍⬩琨椥瑮䴨℩‽⤰瀊楲瑮∨䥆䡇⁔低≗晩猠㈼攠獬⁥⥳','u16')[2:])