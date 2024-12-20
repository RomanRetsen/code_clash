from time import time
from functools import lru_cache

def fib_seq(n):
    cursor0 = 0
    cursor1 = 1
    print(cursor0, cursor1, end=" ")
    for i in range(n-2):
        print(cursor0 + cursor1, end="\n" if i == n-3 else " ")
        cursor0, cursor1 = cursor1, cursor0 + cursor1

def fib_seq_in_list(n):
    result_list = [0, 1]
    for i in range(1, n-1):
        result_list.append(result_list[i-1] + result_list[i])
    print(" ".join([str(x) for x in result_list]))

@lru_cache(None)
def fib_seq_rec(n):
    if n <= 1:
        return n
    else:
        return (fib_seq_rec(n-1) + fib_seq_rec(n-2))

golden_ratio = (1 + 5**0.5)/ 2
golden_ratio_associate = (1 - 5**0.5)/ 2

g_r = (1+5**0.5)/2
g_ar = (1-5**0.5)/2

def nth_fib(n):
    n -= 1
    if n < 50:
        return int((g_r**n - g_ar**n)/5**0.5)
    else:
        if n % 2 == 0:
            n += 2
            return (2*nth_fib(n//2 - 1) + nth_fib(n//2 ))*nth_fib(n//2)
        else:
            return nth_fib(n-1) + nth_fib(n-2)

if __name__ == "__main__":
    t0 = time()
    fib_seq(101)
    t1 = time()
    fib_seq_in_list(101)
    t2 = time()
    for i in range (101):
        print(fib_seq_rec(i), end=" " )
    print()
    t3 = time()

    print(f'fib seq 2 numbers juggling: {t1-t0}')
    print(f'fib seq loops: {t2-t1}')
    print(f'fib seq recur: {t3-t2}')
    print(nth_fib(101))

