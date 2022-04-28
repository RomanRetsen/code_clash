import math


def area_of_circle(circumference):
    area = (circumference * circumference) / (4 * math.pi)
    return area

def area_of_circle2(circumference):
    area = ((circumference / (2 * math.pi)) ** 2) * math.pi
    return area

circumference = int(input(' Please Enter the Circumference of a circle: '))
a = area_of_circle(circumference)
a2 = area_of_circle2(circumference)

print(" Area Of a Circle is ", a)
print(" Area Of a Circle is ", a2)
