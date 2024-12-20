'''
We want to control a robot with a specific set of orders: up down left right.
Sadly our robot doesn't like long statements, it only understands ^ v < >.
Additionally we want to avoid repeating orders, if we have more than one of the same orders, we indicate the repetition with a number after the order: up up up -> ^3
Input
A line containing the orders, separated by spaces.
Output
A line with the compressed orders without spaces.
Constraints
Orders can be: up down left right
Number of orders < 30
Example
Input

up up right down left

Output

^2>v<
--------------------test2
right right right up up up
output
>3^3
-------------------test3
up up down left left up up right down down right right
output
^2v<2^2>v2>2

----------------TEST4
up down down down down right right right right left left left up up up up up up down left left left left right right left right
output
^v4>4<3^6v<4>2<>
---------------------test5
up up up up up up up up up up up up up up up up up up up up up up up up up up up up up
output
^29
'''

# This is THE (regex) WAY OPTION 1
import re

replace_func = lambda x: x.group(1) if len(x.group(0)) == 1 else f"{x.group(1)}{str(len(x.group(0)))}"
elems = {"up":"^", "down":"v", "left":"<", "right":">"}
orders = input().replace(" ", "")
for elem in elems:
    orders = orders.replace(elem, elems[elem])
pattern = r"(.)\1+"
print(re.sub(pattern, replace_func, orders))

# This is THE (regex) WAY OPTION 2
# import re
#
# elems = {"up":"^", "down":"v", "left":"<", "right":">"}
# orders = input().replace(" ", "")
#
# for elem, value in elems.items():
#     orders = orders.replace(elem, value)
#
# while (r := re.search(r"(.)(\1)+", orders)) is not None:
#     s,e = r.span()
#     orders = orders[:s+1] + str(e-s) + orders[e:]
# print(orders)
###########################################

#long and griding....

# elems = {"up":"^", "down":"v", "left":"<", "right":">"}
# orders = input().split()
# multiplier = 0
# current = orders[0]
# result = []
#
# for order in orders:
#     if order == "up":
#         if not current == "up":
#             result.append(elems[current]) if multiplier == 1 else result.append(f"{elems[current]}{multiplier}")
#             multiplier = 1
#             current = order
#         else:
#             multiplier += 1
#     elif order == "down":
#         if not current == "down":
#             result.append(elems[current]) if multiplier == 1 else result.append(f"{elems[current]}{multiplier}")
#             multiplier = 1
#             current = order
#         else:
#             multiplier += 1
#     elif order == "left":
#         if not current == "left":
#             result.append(elems[current]) if multiplier == 1 else result.append(f"{elems[current]}{multiplier}")
#             multiplier = 1
#             current = order
#         else:
#             multiplier += 1
#     elif order == "right":
#         if not current == "right":
#             result.append(elems[current]) if multiplier == 1 else result.append(f"{elems[current]}{multiplier}")
#             multiplier = 1
#             current = order
#         else:
#             multiplier += 1
# else:
#     result.append(elems[current]) if multiplier == 1 else result.append(f"{elems[current]}{multiplier}")
#
#
# print("".join(result))
