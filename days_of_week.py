my_dict = {"Mo":0, "Tu":1, "We":2, "Th":3, "Fr":4, "Sa":5, "Su":6}

difference = input().split("-")
my_list = []
i = my_dict[difference[0]] 
was_in = False
while not i == my_dict[difference[1]] or not was_in == True:
    my_list.append(i)
    was_in = True
    if i >= 6:
        i = 0
    else:
        i += 1
else:
    my_list.append(i)

my_set = set(my_list)
print(my_set)
n = int(input())
r = []
for i in range(n):
    day = input()
    r.append(1 if my_dict[day] in my_set else "no")

print("\n".join(["yes" if x==1 else "no" for x in r]))


# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01
# Test 1
# Input
# Expected output
#
# Mo-Su
# 2
# Tu
# We
#
# yes
# yes
#
# 02
# Test 2
# Input
# Expected output
#
# Mo-Fr
# 3
# Mo
# Fr
# Su
#
# yes
# yes
# no
#
# 03
# Test 3
# Input
# Expected output
#
# Tu-Tu
# 2
# Tu
# Su
#
# yes
# yes
#
# 04
# Test 4
# Input
# Expected output
#
# Mo-Fr
# 4
# Mo
# Mo
# Mo
# Mo
#
# yes
# yes
# yes
# yes
#
# 05
# Test 5
# Input
# Expected output
#
# Sa-Mo
# 3
# Su
# Mo
# Th
#
# yes
# yes
# no
#
#