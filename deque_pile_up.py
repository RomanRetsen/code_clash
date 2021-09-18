from collections import deque

r = []
N = int(input())
for n in range(N):
    NN = int(input())
    cursor = 2**31 + 1
    operational_d = deque([int(x) for x in input().split()])
    for i in range(NN):
        print(f'N {n} and NN {i}; current deque size {len(operational_d)}')
        if operational_d[0] >= operational_d[-1] and operational_d[0] <= cursor:
            cursor = operational_d.popleft()
        elif operational_d[0] <= operational_d[-1] and operational_d[-1] <= cursor:
            cursor = operational_d.pop()
        else:
            r.append(0)
            break
    else:
        r.append(1)

[print("Yes") if x == 1 else print("No") for x in r]