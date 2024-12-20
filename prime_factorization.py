"""
Every number has a unique prime factorisation.
https://www.mathsisfun.com/prime-factorization.html

Example
12 = 2×2×3

2310 = 2×3×5×7×11

For a given input number, your program must output the sum of the numbers in the unique prime factorisation of that number.
Input
Line 1: An integer N greater than 1
Output
1 line The sum of the prime factors of N
Constraints
1<N<15000
Example
Input

60

Output

12

----------
11

11
--------------
1086

186
------------
13230

30

"""


# def is_prime(nmbr):
#     for i in range(1, nmbr):
#         if not i == 1 and nmbr % i == 0:
#             return False
#     return True
#
# def add_prime(prime_list):
#     start_number = prime_numbers[-1] + 1
#     while not is_prime(start_number):
#         start_number += 1
#     prime_list.append(start_number)


#if prime factor is large, this code is slow!!!!!!!!!!!

def add_prime(prime_list):
    start_number = prime_numbers[-1] + 1
    while True:
        for existing_one in prime_list:
            r = divmod(start_number, existing_one)
            if r[1] == 0:
                break
        else:
            prime_list.append(start_number)
            break
        start_number += 1

built = []
prime_numbers = [2]
n = int(input())


while not n == 1:
    current_length_prime_calculated = len(prime_numbers)
    just_added = False
    for i in range(current_length_prime_calculated):
        if n % prime_numbers[i] == 0:
            built.append(prime_numbers[i])
            n //=prime_numbers[i]
            break
    else:
        # if the largest prime number in our storage is smaller than our current numerator
        # add another prime number to the list and run is loop again
        #In the  worst case scenario current numerator IS a prime number (for instance 17)
        while not n % prime_numbers[-1] == 0:
            if n > prime_numbers[-1]:
                add_prime(prime_numbers)
        print(prime_numbers)

# print(sum(built))
print(built)

#-----------------------------------------
def prime_factor(value, offset=0):
    factors = []
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            print("\t" * offset, divisor)
            factors.extend(prime_factor(divisor, offset + 1))
            print("\t" * offset, quotient)
            factors.extend(prime_factor(quotient, offset + 1))
            break
    else:
        factors = [value]
    return factors

#-----------------------------------
def not_using_threading(value):
    factors = []
    i = 2
    while not (r:=divmod(value, i)) == (1,0):
        if r[1] == 0:
            factors.append(i)
            value = r[0]
            i = 2
        else:
            i += 1
    else:
        if len(factors) == 0:
            factors = [value]
        else:
            factors.append(value)
    return factors