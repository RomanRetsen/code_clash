'''


Let's say m = sqrt(n) then m × m = n. Now if n is not a prime then n can be written as n = a × b, so m × m = a × b. Notice that m is a real number whereas n, a and b are natural numbers.

Now there can be 3 cases:

    a > m ⇒ b < m
    a = m ⇒ b = m
    a < m ⇒ b > m

In all 3 cases, min(a, b) ≤ m. Hence if we search till m, we are bound to find at least one factor of n, which is enough to show that n is not prime.

'''
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        print(i)
        if n % i == 0:
            return True
    return False

print(is_prime(21))