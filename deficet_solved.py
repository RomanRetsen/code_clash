from functools import reduce

def defic(x):
    sum = 0
    for i in range(1, x+1, 1):
        if x % i == 0:
            sum += i
    return sum

for _ in range(int(input())):
    start, end = map(lambda x:int(x), input().split(' '))
    # print(sum([x*2-defic(x) for x in range(start, end+1, 1) if x*2 - defic(x) > 0 ]))
    print(reduce(lambda x,y:x + y, [x*2-defic(x) for x in range(start, end+1, 1) if x*2 - defic(x) > 0 ]))

