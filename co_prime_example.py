def is_coprime(x):
    for i in range(2, min(x, 10)):
        if x % i == 0 and 10 % i == 0:
            return False
    return True

def cycle(n):
    if (is_coprime(n)):
        seq = str(1 / n).split('.')[1]
        print(seq)
        q = []
        for i in seq:
            if not i in set(q):
                q.append(i)
            else:
                break
    return len(q)

print(cycle(69))


