from hashlib import sha512
import time


def encrypt_sum_two_numbers(n1, n2):
    numbers_sum = n1 + n2
    return sha512(str(numbers_sum).encode()).hexdigest()

def brute_force_sum_of_two_numbers(hash_input):
    print("Because hash is not possible to decrypt, so we must brute force it")
    time.sleep(5)
    for i in range(1000000):
        print(f"Trying number {i}")
        if (try_hash := sha512(str(i).encode()).hexdigest()) == hash_input:
            print(f"Evrika! The secret sum is {i}")
            break


num1, num2 = [int(x) for x in input("Enter 2 space-separated number\n" \
                                    "(example - '20 12' ) >> ").split()]

hashed_sum = encrypt_sum_two_numbers(num1, num2)
brute_force_sum_of_two_numbers(hashed_sum)
