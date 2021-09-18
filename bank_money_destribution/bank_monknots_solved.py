note_types = [ int(x) for x in input().split(' ')]
n = int(input())

result = {}
for nominal in note_types[::-1]:
    in_exist = n // nominal
    if in_exist:
        result[nominal] = in_exist
        n = n % nominal
    if not n:
        break

for k, value in result.items():
    print(f'{value}x{k}')

# 1 2 5 10 20 50 200 500            - input
# 285                               - output
# 1x200
# 1x50
# 1x20
# 1x10
# 1x5
