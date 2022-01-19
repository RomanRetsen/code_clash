'''
Even the odds
def only_odd_digits(n):
Check that the given positive integer n contains only odd digits (1, 3, 5, 7 and 9) when it is written
out. Return True if this is the case, and False otherwise. Note that this question is not asking
whether the number n itself is odd or even. You therefore will have to look at every digit of the given
number before you can proclaim that the number contains no odd digits.
To extract the lowest digit of a positive integer n, use the expression n%10. To chop off the lowest
digit and keep the rest of the digits, use the expression n//10. Or, if you don't want to be this fancy,
you can irst convert the number into a string and work from there with string operations.
n Expected result
8 False
1357975313579 True
42 False
71358 False
0 False
'''
def only_odd_digits(n):
    while (new_n := n // 10) > 0:
        if n % 10 % 2 == 0:
            print("False")
            break
        n = new_n
    else:
        if n % 10 % 2 == 0:
            print("False")
        else:
            print("True")

the_num = int(input())
only_odd_digits(the_num)