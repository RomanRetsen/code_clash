"""

Input
Expected output

2
B*3 7

21 7

02
Test 2
Input
Expected output

3
1 999 10

1 999 10

03
Test 3
Input
Expected output

2
50 A*2

50 100

04
Test 4
Input
Expected output

6
E*5 D*3 1 C*2 B*4 A*6

120 6 1 2 24 720

05
Test 5
Input
Expected output

5
C*3 D*7 5 3 A*2

15 21 5 3 30

"""

#my variant

# n = int(input())
# my_dict = {}
# start_point = 64
# for index, column in enumerate(input().split(), 1):
#     my_dict[chr(start_point + index)] = column
# 
# print(my_dict)
# for i in range(n):
#     for k, v in my_dict.items():
#         for char in v:
#             if char in my_dict:
#                 my_dict[k] = v.replace(char, my_dict[char])
#                 try:
#                     my_dict[k] = str(eval(my_dict[k]))
#                 except NameError:
#                     pass
# 
# print(*[v for v in my_dict.values()])


#AgathokakologicalBit variant
n = int(input())
cols = [c.split('*') for c in input().split()]
cols = [int(c[0]) if len(c) == 1 else [c[0], int(c[1])] for c in cols]
print(cols)
while any(type(c) is not int for c in cols):
    cols = [
        c if type(c) is int
        else (c[1]*cols[ord(c[0])-ord('A')]
        if type(cols[ord(c[0])-ord('A')]) is int
        else c)
        for c in cols
    ]

print(*cols)
