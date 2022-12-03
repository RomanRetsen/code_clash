'''
Line 1: The size N of the grid.
Line 2: The number of words W.
Next W lines: The word list.
Output
One line with the two diagonal words, space separated and in alphabetical order.
Constraints
3 ≤ N ≤ 20
W ≤ 100
Example
Input

3
3
cow
bat
rat

Output

cat war

--------------test2


5
5
sack
cute
harbour
skull
elite

output

choke stole

----------------test3


8
10
magical
academy
bail
reasoning
golden
alliance
auto
negotiate
alert
angel

output

absolute marginal

-------------------------test4


15
36
tackle
absent
fake
racial
absurd
icon
ultimate
annually
sack
abundance
abstract
challenging
wander
abuse
acid
domain
academy
accordance
accelerate
tactic
accent
ease
habitat
amid
acre
aide
accountable
banner
adequate
acute
aids
absorb
adverse
sacred
alert
bass

kindheartedness trustworthiness


'''

r1 = []
r2 = []
n = int(input())
w = int(input())
temp_n = 0
# temp_n2 = 0
for i in range(w):
    row = input()
    for letter in row:
        if temp_n == 0:
            r1.append(letter)
            temp_n += 1
        elif temp_n == n - 1:
            r2.append(letter)
            temp_n += 1
        elif temp_n == n:
            temp_n = 0
        else:
            temp_n += 1

        # if temp_n2 == n - 1:
        #     r2.append(letter)
        #     temp_n2 -= 1
        # elif temp_n == n:
        #     temp_n = 0
        # else:
        #     temp_n += 1

print("".join(r1))
print("".join(r2))
