"""
You receive many fruits, and you have to make juice from it.

You are given the number of types of fruit you receive (N), then the name (as a character, c) followed by how many fruit you need to create a glass of juice n.
Finally, you receive a list of fruits LINE (represented by their character c).

With the given fruits, how many full glass of juice you can make?

Note: We do not mix different fruits into one juice. That would be barbaric.
Input
Line 1: An integer N for the number of types of different fruit.
Next N lines: N type of fruit (as c), and after a space the number of fruits you need for one glass of juice n
Last line: LINE, the list of your fruits.
Output
Line 1: Number of full glass of juices you can produce.
Constraints
1 < N < 30
1 < n < 9
Example
Input

1
F 3
FFFFFF

Output

2
----------test 2
2
F 3
A 4
FFFFFFAAAAAA

ouput

3
--------test3
5
R 2
E 1
F 9
A 7
S 3
SEFRAREFASSREAFRAESRFARSERAFRASEARFFFF

output

14
------------test4 - A lot of juice
26
A 8
B 2
C 4
D 3
E 2
F 1
G 2
H 6
I 5
J 4
K 3
L 9
M 5
N 6
O 7
P 8
Q 4
R 3
S 2
T 4
U 5
V 6
W 3
X 2
Y 1
Z 8
IMAGINEWASYOUREMOVALRAISINGGRAVITYUNSATIABLEUNDERSTOODOREXPRESSIONDISSIMILARSOSUFFICIENTITSPARTYEVERYHEARDANDEVENTGAYADVICEHEINDEEDTHINGSADIEUSINNUMBERSOUNEASYTOMANYFOURFACTINHEFAILMYHUNGITQUITNEXTDOOFITFIFTEENCHARMEDBYPRIVATESAVINGSITMRFAVOURABLECULTIVATEDALTERATIONENTREATIESYETMETSYMPATHIZEFURNITUREFORFEITEDSIROBJECTIONPUTCORDIALLYCONTINUEDSPORTSMEN

output
108
"""


recipe_dict = {}
counter_dict = {}
general_counter = 0

n = int(input())
for i in range(n):
    inputs = input().split()
    c = inputs[0]
    n = int(inputs[1])
    recipe_dict[c] = n
    counter_dict[c] = 0
line = input()
for l in line:
    counter_dict[l] += 1
for k,v in counter_dict.items():
    general_counter += v // recipe_dict[k]

print(general_counter)

"""
#other person1 code. Use of string's count
n = int(input())
l = []
for i in range(n):
    inputs = input().split()
    l.append((inputs[0],int(inputs[1])))
    
line = input()

m = 0
for a, b in l:
    m += math.floor(line.count(a)/b)
print(m)
"""

"""
#other person2 code. Use of collections Class Counter
from collections import Counter


n = int(input())
cost={}
for i in range(n):
    inputs = input().split()
    cost[inputs[0]] = int(inputs[1])
cnt=Counter(input())

sumadsfads=0
for x,y in cnt.items():
  sumadsfads += y//cost[x]
print(sumadsfads)
"""