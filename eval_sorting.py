from math import*
R=range
a,b=map(int,input().split())
[*map(print,sorted([f'{i}/{j}'for j in R(a,b+1)for i in R(1,j)if gcd(i,j)<2],key=eval))]

