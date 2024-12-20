import math

m=100000+1
r=int(math.sqrt(m))
p = [True]*m
print(r)
for i in range(2,r):
    if p[i]:
        for j in range(i+i,m,i):
            p[j]=False

n = int(input())

r=0
for i in range(2, n):
    if p[i]:r+=1
print(r)
