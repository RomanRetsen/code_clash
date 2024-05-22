import itertools
import random
import functools


my_list = [random.randint(1, 100) for _ in range(20)]
print(my_list)

l = len(my_list)
for i in range(l):
    for y in range(l-i-1):
        if my_list[y] > my_list[y+1]:
            my_list[y], my_list[y+1] = my_list[y+1], my_list[y]
print(my_list)
print(list(itertools.accumulate(my_list, lambda x,y:y-x)))
print([my_list[y+1]-my_list[y] for y in range(len(my_list)-1)])