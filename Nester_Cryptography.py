from cryptography.fernet import Fernet


class NesterEncryptSum:
    def __init__(self):
        key = Fernet.generate_key()
        self.fernet = Fernet(key)
        self.encMessage = None
        self.num1 = None
        self.num2 = None

    def encrypt_sum_two_numbers(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
        numbers_sum = n1 + n2
        self.encMessage = self.fernet.encrypt(str(numbers_sum).encode())

    def decrypt_sum_two_numbers(self, hash_input):
        if self.encMessage:
            return self.fernet.decrypt(self.encMessage).decode()
        else:
            print("ERROR! No message was provided")


# Testing newly created class
num1, num2 = [int(x) for x in input("Enter 2 space-separated number\n" \
                                    "(example - '20 12' ) >> ").split()]
my_encryp = NesterEncryptSum()
my_encryp.encrypt_sum_two_numbers(num1, num2)
print(f"Encrypted sum of two numbers \
    ({my_encryp.num1} and {my_encryp.num2}) {my_encryp.encMessage}")
decrypted_message = my_encryp.decrypt_sum_two_numbers(my_encryp.encMessage)
print(decrypted_message)

