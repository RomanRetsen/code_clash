
import itertools

chosen = 10000
t = []
r, c = [int(i) for i in input().split()]
for i in range(r):
    t.append([int(x) for x in input().split(' ')])
p = [x for x in itertools.product([-1,1,0], [-1,1,0])]
p.remove((0,0))

for x in range(1,r-1):
    for y in range(1,c-1):
        if t[x][y] < min([t[x+a][y+b] for a,b in p ]) and t[x][y] < chosen:
            chosen = t[x][y]

print(chosen)

# input
# 4 4
# 4 5 6 6
# 6 3 5 2
# 4 7 1 2
# 4 8 2 5
#
# output
# 1
