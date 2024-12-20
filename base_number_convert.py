
import string

# convert 10-based number into 26-based number where 0 converts to A, 1 - B, 25 - Z
convert_table = {a:b for a,b in zip(range(26), string.ascii_uppercase)}
convert_table_rev = {b:a for a,b in zip(range(26), string.ascii_uppercase)}
n = int(input())
result = []
while (new_n := n // 26) > 0:
    result.append(convert_table[n % 26])
    n = new_n
else:
    result.append(convert_table[n])
r = "".join(reversed(result))
print(r)

print("check reverse")

ten_base_number = 0
for index, number in enumerate(str(r)[::-1]):
    ten_base_number += (convert_table_rev[number]  * (26 ** index))
    print(index, number)

print(f"result of server back {ten_base_number}")

"""
25

Z
--------
35

BJ
-----------
2

C

-----------
321274

SHGS

--------
26

BA
"""