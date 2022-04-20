import itertools
import string
import random


the_list = [random.randint(0, 1000) for _ in range(25)]

print(list(itertools.accumulate(the_list, max)))