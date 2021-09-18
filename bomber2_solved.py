z=input
width = int(z())
height = int(z())
field = []
damage = 0
index_x = -1
index_y = -1
for row_index in range(height):
    [field.append(int(x)) for x in input()]
print(field)

for a in range(height -2 ):
    for b in range(width - 2):
        data = [
                field[a * width + b], field[a * width + 1 + b], field[a * width + 2 + b],
                field[(a + 1) * width + b], field[(a + 1) * width + 1 + b], field[(a + 1) * width + 2 + b],
                field[(a + 2) * width + b], field[(a + 2) * width + 1 + b], field[(a + 2) * width + 2 + b]
                ]
        current_damage = sum(data)
        if not 'A' in data and current_damage > damage:
            damage = current_damage
            index_x = b + 1
            index_y = a + 1

print(f'{damage}')
print(f'{index_x} {index_y}')
