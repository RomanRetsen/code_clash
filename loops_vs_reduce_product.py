import itertools
import functools
from time import time

t0 = time()
seq = range(1, 10000, 1)
s = 0
for i in seq:
    for y in seq:
        s += y*i

print(s)
t1 = time()
print(functools.reduce(lambda x,y:x+y, [x*y for x,y in itertools.product(seq, repeat=2)]))
t2 = time()


print(f'loops time: {str(t1-t0)}')
print(f'reduce product comprehention time: {str(t2-t1)}')
