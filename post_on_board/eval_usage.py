'''

The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
01
Test 1
Input
Expected output

2 ? 9 = 11

+

02
Test 2
Input
Expected output

22 ? 2 = 11

/

03
Test 3
Input
Expected output

78 ? 42 = 3276

*

04
Test 4
Input
Expected output

47 ? 28 = 19

-
'''
# my solution

left, right = input().split(" = ")

if eval(left.replace("?", "+")) == int(right):
    print("+")
elif eval(left.replace("?", "-")) == int(right):
    print("-")
elif eval(left.replace("?", "*")) == int(right):
    print("*")
elif eval(left.replace("?", "/")) == int(right):
    print("/")

#------------------------------------------
# other guy's even more clever one
# exp = input()
# for operation in "+-*/":
#     if eval(exp.replace("?", operation).replace("=", "==")):
#         print(operation)
#         break
