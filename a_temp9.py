import re
import string

the_value = input("Entered password")
l_the_value = len(the_value)
points = 0

if l_the_value < 8:
    points += -1
elif l_the_value < 12:
    points += 2
elif l_the_value < 15:
    points += 3
else:
    points += 4

if any([x for x in the_value if x in string.ascii_lowercase]):
    points += 1
if any([x for x in the_value if x in string.ascii_uppercase]):
    points += 1
if any([x for x in the_value if x in string.digits]):
    points += 1
if any([x for x in the_value if x in "!#$%^&"]):
    points

print(f"Points: {points}")
