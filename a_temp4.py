'''
You are given 3 integers x, y, and z. Return x raised to the power of y modulo z. If the operation is invalid, return "undefined".

For example:
Given 10, 2, 99. Return 1. Since (10 ^ 2) mod 99 = 100 % 99 = 1.

Hint:
Notice how (a * a) % b = ((a % b) * (a % b)) % b.
Input
Line 1: An integer x
Line 1: An integer y
Line 1: An integer z
Output
Line 1 : An integer that is modulo z of x ^ y.
---------------------------------------------

1987654321
1123456789
88888888
output
65130937
--------------------------------------------


123
456
789
output
699


'''
def pow_mod(B, E, M):
    print(f"x{B}-y{E}-z{M}")
    if E == 0:
        print(f"returning1 1")
        return 1
    elif E == 1:
        print(f"returning2 {B % M}")
        return B % M
    else:
        root = pow_mod(B, E // 2, M)
        if E % 2 == 0:
            print(f"returning3 {root * root % M}")
            return (root * root) % M
        else:
            print(f"returning4 {(root * root * B) % M}")
            return (root * root * B) % M

x = int(input())
y = int(input())
z = int(input())
print(pow_mod(x, y, z))