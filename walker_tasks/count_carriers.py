'''
Carry on Pythonista
def count_carries(a, b):
Two positive integers a and b can be added with the usual integer column-wise addition algorithm
that we all learned as wee little children so early that most people don't even think of that
mechanistic operation as an algorithm! Instead of the sum a+b that the language would already
compute for you anyway, this problem asks you to count how many times there will be a carry of
one into the next column during this mechanistic addition. Your function should be ef icient even for
behemoths that consist of thousands of digits.
To extract the lowest digit of a positive integer n, use the expression n%10. To extract all other digits
except the lowest one, use the expression n//10. You can use these simple integer arithmetic
operations to traipse through the steps of the column-wise integer addition where you don't care
about the actual result of the addition, but only tally up the carries produced in each column as
proof of work of you actually labouring through the steps of the column-wise addition.
b Expected result
0 0 0
99999 1 5
11111111111 2222222222 0
123456789 987654321 9
2**100 2**100 - 1 13
10**1000 - 123**456 123**456 1000
'''
'''
def count_carries(a, b):
    carrier_dump = 0
    carrier_counter = 0
    try_once = True
    while a // 10 > 0 and b // 10 > 0:
        carrier_dump = (a % 10 + b % 10 + carrier_dump) // 10
        if carrier_dump > 0:
            carrier_counter += 1
        a = a // 10
        b = b // 10
    else:
        print(a, b, carrier_dump, carrier_counter)
        while (a // 10 > 0 or b // 10 > 0) and try_once:
            carrier_dump = (a % 10 + b % 10 + carrier_dump) // 10
            if carrier_dump > 0:
                carrier_counter += 1
            else:
                try_once = False
            a = a // 10
            b = b // 10
        else:
            if (a%10 + b%10 + carrier_dump ) // 10 > 0:
                carrier_counter += 1
    return carrier_counter

'''

# better shorter version. same
def count_carries(a, b):
    carrier_dump = 0
    carrier_counter = 0
    try_once = True
    while (a // 10 > 0 or b // 10 > 0) and try_once:
        carrier_dump = (a % 10 + b % 10 + carrier_dump) // 10
        a = a // 10
        b = b // 10
        if carrier_dump > 0:
            carrier_counter += 1
        elif any((a == 0, b == 0)):
            try_once = False
    else:
        if (a % 10 + b % 10 + carrier_dump ) // 10 > 0:
            carrier_counter += 1
    return carrier_counter

a = 10**1000 - 123**456
b = 123**456
print(count_carries(a, b))
a = 2**100
b = 2**100 - 1
print(count_carries(a, b))
a = 123456789
b = 987654321
print(count_carries(a, b))
a = 11111111111
b = 22222222222
print(count_carries(a, b))
a = 99999
b = 1
print(count_carries(a, b))
a = 0
b = 0
print(count_carries(a, b))
a = 1544
b = 228
print(count_carries(a, b))
a = 95
b = 222222
print(count_carries(a, b))
a = 97763
b = 9733333

print(count_carries(a, b))