i = input
h,d=[int(x) for x in i().split()]
n=int(i())
enemies = []
for x in range(n):
    eh,ed=[int(x) for x in i().split()]
    enemies.append((eh,ed))
r = sum([x[1]*((x[0]-1)//d)+sum([o[1] for o in enemies[index+1:]])+((x[0]-1)//d)*sum([o[1] for o in enemies[index+1:]]) for index, x in enumerate(enemies)])

print(['fight','flee'][h < r] )
# itertools.accumulate([x[1]*x[0]//d for x in enemies if x[0] < d], lambda x:sum(enemies[]))
# functools.reduce(lambda x,y:x-y, )