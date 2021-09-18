char_list = [int(x) for x in input()]
n = int(input())
my_map = {x:[] for x in char_list}
for i in range(n):
    for index, value in enumerate([x for x in input()]):
        if value.isdigit():
            my_map[int(value)].append((index, i))
print(my_map)
for key, value in my_map.items():
    print(f'{key}:', ', '.join([str(x)+' '+str(y) for x,y in value ]))





# 12345678
# 3
# ...1..........5.....
# ...............5....
# ....7.......3...2...