import functools


#input 3 32 12 50
i = "3 32 12 50".split()

#flattaning the numbers of numbers
r = [x for y in i for x in y ]
print(r)
#['3', '3', '2', '1', '2', '5', '0']

#sum of numbers of each number
r2 = [sum([int(x)for x in y])for y in i]
#[3, 5, 3, 5]
print(r2)
print(functools.reduce(lambda x,y:x*y,r2))
#225


#re-arrange list of list in 90 degree
mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
r3 = [[row[i] for row in mat] for i in range(len(mat[0]))]
print(r3)
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print(eval("*".join([f'({"+".join(x)})' for x in i])))
#eval igenerated input is (3)*(3+2)*(1+2)*(5+0)