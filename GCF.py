from random import randint
from time import time
from functools import reduce
from math import gcd

def list_of_factor(x_input):
    return set([x for x in range(1, x_input + 1) if x_input % x == 0])

def gcf_list(input_list):
    the_base = list_of_factor(input_list[0])
    all_options = {}
    for i in input_list[1::]:
        all_options[i] = list_of_factor(i)
    for y in all_options:
        the_base &= all_options[y]
    return max(the_base)

def gcf_list(input_list):
    return reduce(gcd, input_list)

if __name__ == "__main__":
    my_list = [randint(1,1000000) for _ in range(1000000)]
    print(gcf_list(my_list))
    print(gcf_list(my_list))