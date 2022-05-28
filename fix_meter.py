import time
import re
def faulty_odometer_instant(n):
    denominators = {100000000: [56953279, 8],
                    10000000: [5217031, 7],
                    1000000: [468559, 6],
                    100000: [40951, 5],
                    10000: [3439, 4],
                    1000: [271, 3],
                    100: [19, 2],
                    10: [1, 1]
                    }
    total  = 0
    operational_n = n
    for level in denominators:
        # print(operational_n)
        if (result := divmod(operational_n, level))[0] > 0:
            total += result[0] * denominators[level][0]
            if result[0] > 4:
                total += 9 ** denominators[level][1]
            operational_n = result[1]
    else:
        if result[1] > 4:
            total += 1
    return n - total

def faulty_odometer(n):
    regex = re.compile(r'4')
    count = 0
    for i in range(0, n):
        if regex.search(str(i)):
            count += 1
        else:
            pass
    return n - count

#4104
def faulty_odometer_improved(n):
    start = 0
    count = 0
    while start < n:
        start += 1
        start_as_str = str(start)
        if "4" in str(start):
            correction = 10 ** (len(start_as_str) - start_as_str.index("4") - 1)
            start += correction
            count += correction
    return n - count

a = 500
t0 = time.time()
result = faulty_odometer(a)
print(f"result from original (Lopez) function {result}. Time taken {time.time() - t0}")

# t1 = time.time()
# result = faulty_odometer_improved(a)
# print(f"result from improved (Lopez) function {result}. Time taken {time.time() - t1}")
#
# t2 = time.time()
# result = faulty_odometer_instant(a)
# print(f"result from instant result function {result}. Time taken {time.time() - t2:f}")
