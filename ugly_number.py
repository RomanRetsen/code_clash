import time


def is_ugly(l):
    while l > 1:
        if l % 5 == 0:
            l //= 5
        elif l % 3 == 0:
            l //= 3
        elif l % 2 == 0:
            l //= 2
        else:
            break
    return True if l == 1 else False

def max_devide(number, devisor):
    while number % devisor == 0:
        number /= devisor
    return number

def is_ugly(number):
    number = max_devide(number, 2)
    number = max_devide(number, 3)
    number = max_devide(number, 5)
    return 1 if number == 1 else 0

def nth_ugly_number2(n):
    i = 1

    count = 1
    while n > count:
        i += 1
        if is_ugly(i):
            count += 1
    return i

def nth_ugly_number(n):
    c = 1
    i = 2
    the_number = 1
    while c < n:
        if is_ugly(i):
            c +=1
            the_number = i
        i += 1
    return the_number

def nth_ugly_number3(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        print(ugly)
        print(f'i2i3i5{i2} {i3} {i5} ')
        print(f'next{next_multiple_of_2} {next_multiple_of_3} {next_multiple_of_5} ')
        ugly [i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        if ugly[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        if ugly[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
        if ugly[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    return ugly[-1]

    print(ugly)

if __name__ == "__main__":
    n = int(input())

    t0 = time.time()
    print(nth_ugly_number(n))
    t1 = time.time()
    print(nth_ugly_number2(n))
    t2 = time.time()
    print(nth_ugly_number3(n))
    t3 = time.time()

    print(f'My vertion: {t1-t0}')
    print(f'other vertion: {t2 - t1}')
    print(f'other vertio2: {t3 - t2}')
