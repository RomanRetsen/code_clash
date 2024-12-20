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
def is_prime(nmbr):
    for i in range(1, nmbr):
        if not i == 1 and nmbr % i == 0:
            return False
    return True

def add_prime(prime_list):
    start_number = prime_numbers[-1] + 1
    while not is_prime(start_number):
        start_number += 1
    prime_list.append(start_number)

built = []
prime_numbers = [2]
n = int(input())


while not n == 1:
    current_length_prime_calculated = len(prime_numbers)
    for i in range(current_length_prime_calculated):
        if n % prime_numbers[i] == 0:
            built.append(prime_numbers[i])
            n //=prime_numbers[i]
            break
    else:
        # if the largest prime number in our storage is smaller than our current numerator
        # add another prime number to the list and run is loop again
        #In the  worst case scenario current numerator IS a prime number (for instance 17)
        if n > prime_numbers[-1]:
            add_prime(prime_numbers)

print(sum(built))
