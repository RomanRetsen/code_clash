
n = int(input())
counter = 1
points = []
for i in range(n):
    x, y = [float(j) for j in input().split()]
    points.append((x,y))
result = []
first_in = False
atleast_one_not = False
print(points)
while True:
    atleast_one_not = False
    for i in range(len(points)):
        for y in range(len(points)):
            if not y == i:
                distance = ((points[y][0] - points[i][0]) ** 2 + (points[y][1] - points[i][1]) ** 2) ** 0.5
                print(f'distance {distance}')
                if distance <= (counter * 2) and not first_in:
                    result.append(counter)
                    first_in = True
                elif distance > (counter * 2):
                    atleast_one_not = True


    if not atleast_one_not:
        result.append(counter)
        break
    counter += 1

print(*result)
