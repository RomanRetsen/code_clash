"""
You have a set of strings.
Find the matching ends (first and last characters of the strings) and connect them together,
essentiolly building single string out of it.
Out of 2 connecting characters from concatenation of 2 strings, only one remaining .
Meaning string "A------X" joining string "X====*" resulting in A------X====*

-------------test1

4
A------X
*-+-+-+-+-+-+-#
X====*
#_____Z

out

A------X====*-+-+-+-+-+-+-#_____Z

----------------test 2


2
+...........Z
A..............+

out

A..............+...........Z


-----------Test 3

10
'.
:Z
-*
.,
,:
=/
/'
A+
+-
*=

out

A+-*=/'.,:Z


------------Test 4


3
-----+++++++++
A------
++++++=======Z

A----------++++++++++++++=======Z



-------------- Test 5

1
A_-_-_-_-_-_-_Z

out

A_-_-_-_-_-_-_Z





"""


import collections


result = collections.deque()
n = int(input())
all_parts = []
for i in range(n):
    spaghetti_part = input()
    all_parts.append([spaghetti_part, False])

result.append(all_parts[0][0])
all_parts[0][1] = True
unassign_list = [(index, x[0], x[1]) for index, x in enumerate(all_parts) if x[1] == False]

while len(unassign_list) > 0:
    for part in unassign_list:
        if part[1][0] == result[-1][-1]:
            result.append(part[1][1:])
            all_parts[part[0]][1] = True
        elif part[1][-1] == result[0][0]:
            result.appendleft(part[1][:-1])
            all_parts[part[0]][1] = True
    unassign_list = [(index, x[0], x[1]) for index, x in enumerate(all_parts) if x[1] == False]

print(*result, sep="")