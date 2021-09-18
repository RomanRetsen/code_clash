temp=[bin(ord(x))[2:]for x in input()]
print(*[''.join([a[m]for a in temp])for m in range(7)],sep='\n')
# [[print(a[m], end='') for a in [bin(ord(x))[2:] for x in input()]for m in range(7)] for m in range(7)]


# print([[y[n]  for y in [bin(ord(x))[2:]  for x in input()]] for n in range(7)])

# sorted_list = [bin(ord(x))[2:] for x in input()]
# for i in range(7):
#     for word in sorted_list:
#         print(word[i], end='')
#     print()

# v=[bin(ord(x))[2:] for x in input()]
# final_list = [[] for _ in range(7)]
# for value in v:
#     for index, letter in enumerate(value):
#         final_list[index].append(letter)
#
# print(*[''.join(x) for x in final_list], sep='\n')

# Example
# 1111111
# 0111111
# 0100100
# 0101010
# 1001011
# 0000000
# 1011001
#
#