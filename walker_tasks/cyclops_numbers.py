'''
Cyclops numbers
def is_cyclops(n):
A nonnegative integer is said to be a cyclops number if it consists of an odd number of digits so
that the middle (more poetically, the “eye”) digit is a zero, and all other digits of that number are
nonzero. This function should determine whether its parameter integer n is a cyclops number, and
return either True or False accordingly.
n Expected result
0 True
101 True
98053 True
777888999 False
1056 False
675409820 False
As an extra challenge, you can try to solve this problem using only loops, conditions and integer
arithmetic operations, without irst converting the integer into a string and working from there.
Dividing an integer by 10 with the integer division // effectively chops off its last digit, whereas the
remainder operator % can be used to extract that last digit. These operations allow us to iterate
through the digits of an integer one at the time from lowest to highest, almost as if that integer were
some kind of lazy sequence of digits.
Even better, this operation doesn't work merely for the familiar base ten, but it works for any base
by using that base as the divisor. Especially using two as the divisor instead of ten allows you to
iterate through the bits of the binary representation of any integer, which will come handy in
problems in your later courses that expect you to be able to manipulate these individual bits. (In
practice these division and remainder operations are often further condensed into equivalent but
faster bit shift and bitwise and operations.)

'''


def is_cyclops(in_value):
    left_side = 0
    right_side = 0
    eye_passed = False

    while (new_value := in_value // 10) > 0:
        tail = in_value % 10
        if tail == 0 and eye_passed:
            return "False"
            break
        elif tail == 0 and not eye_passed:
            eye_passed = True
        elif not tail == 0 and not eye_passed:
            right_side += 1
        elif not tail == 0 and eye_passed:
            left_side += 1
        in_value = new_value
    else:
        if not in_value % 10 == 0:
            left_side += 1

        if left_side == right_side:
            return "True"
        else:
            return "False"


in_value = int(input())
print(is_cyclops(in_value))


