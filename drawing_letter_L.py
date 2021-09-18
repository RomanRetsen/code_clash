w, h = [int(i) for i in input().split(' ')]
x, y = [int(i) for i in input().split(' ')]

# generating chunks
if ((x - 1) % 2 == 1):
    top_filler_1 = 'XO' * ((x - 1) // 2) + 'X'
    top_filler_2 = 'OX' * ((x - 1) // 2) + 'O'
elif ((x - 1) % 2 == 0):
    top_filler_1 = 'XO' * (x // 2)
    top_filler_2 = 'OX' * (x // 2)

if ((w - 2) % 2 == 1):
    bottom_filler_1 = 'XO' * ((w - 2) // 2) + 'X'
    bottom_filler_2 = 'OX' * ((w - 2) // 2) + 'O'
elif ((w - 2) % 2 == 0):
    bottom_filler_1 = 'XO' * ((w - 1) // 2)
    bottom_filler_2 = 'OX' * ((w - 1) // 2)

#drawing L
print(('-'*(x-1)).center(x+1, '+'))

for iter in range(1, y+1, 1):
    if iter % 2 == 1:
        if iter == y:
            print(top_filler_1.rjust(x, '|')+('-'*(w-x-2)).center(w-x, '+'))
        else:
            print(top_filler_1.center(x+1, '|'))
    else:
        if iter == y:
            print(top_filler_2.rjust(x, '|')+('-'*(w-x-2)).center(w-x, '+'))
        else:
            print(top_filler_2.center(x+1, '|'))

for iter2 in range(1, h-y-1, 1):
    if iter % 2 == 0:
        if iter2 % 2 == 0:
            print(bottom_filler_2.center(w, '|'))
        else:
            print(bottom_filler_1.center(w, '|'))
    else:
        if iter2 % 2 == 0:
            print(bottom_filler_1.center(w, '|'))
        else:
            print(bottom_filler_2.center(w, '|'))
print(('-'*(w-2)).center(w, '+'))

#example for
# 9 6
# 5 2
print("+----+")
print("|XOXO|")
print("|OXOX+--+")
print("|XOXOXOX|")
print("|OXOXOXO|")
print("+-------+")
