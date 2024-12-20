import random, heapq, time


def find_2_largest(input_list):
    result1 = result2 = -1
    for i in input_list:
        if (current_min := min(result1, result2)) < i:
            if result1 == current_min:
                result1 = i
            else:
                result2 = i
    return (result1, result2)

def find_2_largest2(input_list):
    result1 = result2 = -1
    for i in input_list:
        if result2 < i:
            result2 = i
        elif result1 < i:
            result1 = i
    return (result1, result2)

nums = [random.randint(0, 100000000) for _ in range(10000000)]
t0 = time.time()
print(sorted(nums)[-2:])
print(f"time needed for searching 2 largest numbers after sorting : {time.time() - t0}")

t1 = time.time()
print(heapq.nlargest(2, nums))
print(f"time needed for searching 2 largest numbers using heap!!! : {time.time() - t1}")

t2 = time.time()
print(find_2_largest(nums))
print(f"time needed for manual search of largest 2 numbers {time.time() - t2}")

t3 = time.time()
print(find_2_largest2(nums))
print(f"time needed for manual search of largest 2 numbers {time.time() - t3}")
