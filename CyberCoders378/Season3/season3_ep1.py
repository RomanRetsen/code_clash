import time

total = 0
time1 = time.time()
with open("input.txt") as file:
    for line in file:
        temp = line.strip()
        l = len(temp)//2
        # for i in range(l):
        #     if not temp[i] == temp[-i-1]:
        #         break
        # else:
        #     total += 1
        if temp[:l] == temp[::-1][:l]:
            total += 1
time2 = time.time()

print(time2 - time1)
