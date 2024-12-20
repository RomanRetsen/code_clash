import sys
from itertools import groupby

l = int(input())
s = sorted(input())
print(s, file=sys.stderr)

groups = ["".join(g[1]) for g in groupby(s)]
print(groups, file=sys.stderr)

odd_element = ''

r = ""
for e in groups:
    le = len(e)
    if le > 1:
        r += e[0] * (le // 2)
    if le % 2 == 1 and odd_element == '':
        odd_element = e[0]
r += odd_element + r[::-1]
print(r)
