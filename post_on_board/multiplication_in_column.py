"""
 Test 1
Input
Expected output


123
45

 123
x 45
----
 615
4920
----
5535

02
Test 2
Input
Expected output

9050
308

   9050
  x 308
-------
  72400
2715000
-------
2787400

03
Test 3
Input
Expected output

5
3

  5
x 3
---
 15
---
 15

04
Test 4
Input
Expected output

54321
9876

    54321
   x 9876
---------
   325926
  3802470
 43456800
488889000
---------
536474196
"""
oper_1 = int(input())
oper_2 = int(input())
result = oper_1 * oper_2
l = max(len(str(oper_1 * oper_2)), len(f"x {str(oper_2)}"))

print(str(oper_1).rjust(l, " "))
print(f"x {str(oper_2)}".rjust(l, ' '))

print("-" * l)
for index, i in enumerate(str(oper_2)[::-1]):
    if not i == "0":
        print(str(int(i) * oper_1 * (10 ** int(index))).rjust(l, " "))

print("-" * l)
print(str(result).rjust(l, " "))
