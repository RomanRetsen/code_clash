def approach_center(index):
    if list_of_throwers[index][0] > 10:
        list_of_throwers[index][0] -= 1
    elif list_of_throwers[index][0] < 10:
        list_of_throwers[index][0] += 1
    if list_of_throwers[index][1] > 10:
        list_of_throwers[index][1] -= 1
    elif list_of_throwers[index][1] < 10:
        list_of_throwers[index][1] += 1

n_throwers = int(input())
list_of_throwers = []
for _ in range(n_throwers):
    x, y = input().strip().split(' ')
    list_of_throwers.append([int(x), int(y), 1])

while list_of_throwers:
    safe = True
    for index, item in enumerate(list_of_throwers):
        if item[0] == 10 and item[1] == 10:
            safe = False
            item[2] = 0 # changing object status to "delete for next round"
        else:
            approach_center(index)
    if safe:
        print('STAND UP')
    else:
        print('CRUCH')
    list_of_throwers = [x for x in list_of_throwers if x[2] == 1]
print('STAND UP')

