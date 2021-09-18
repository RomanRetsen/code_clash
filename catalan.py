import time
import math


def catalan(n):
    if n <= 1:
        return 1
    s = 0
    for i in range(n):
        s += catalan(i) * catalan(n-i-1)
    return s

def catalan2(n):
    return (math.factorial(2*n) / (math.factorial(n+1) * math.factorial(n)))

t0 = time.time()
for i in range(17):
    print(f'{catalan(i):g}', end="\t")
t1 = time.time()
print(f'Recursion: {t1-t0}')

t2 = time.time()
for i in range(17):
    print(f'{catalan2(i):g}', end="\t")
t3 = time.time()
print(f'Not Recursion: {t3-t2}')
