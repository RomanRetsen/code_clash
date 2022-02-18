def collect_numbers(perm):
    counter = 1
    start = perm[0]
    for i in range(1, len(perm)):
        if perm[i] < start:
            counter += 1
        start = perm[i]
    return counter

the_list = [8, 6, 9, 5, 4, 11, 2, 0, 3, 10, 12, 1, 7]
# the_list = list(range(10**6, -1, -1))
print(collect_numbers(the_list))