z=input
width = int(z())
height = int(z())
field = []
damage = 0
the_x = -1
the_y = -1
for row_index in range(height):
    field.append([int(x) for x in input()])
print(field)
for i in range(1, width-1):
    for y in range(1, height-1):
        print(f'[{i}-{y}')
        if not 'A' in [field[i][y], field[i][y-1], field[i][y+1],
                       field[i-1][y], field[i-1][y-1], field[i-1][y+1],
                       field[i+1][y-1], field[i+1][y], field[i+1][y+1]]:
            this_sum = sum([field[i][y], field[i][y-1], field[i][y+1],
                       field[i-1][y], field[i-1][y-1], field[i-1][y+1],
                       field[i+1][y-1], field[i+1][y], field[i+1][y+1]])
            if this_sum > damage:
                damage = this_sum
                the_x = i
                the_y = y

print(f'{the_x} {the_y}')