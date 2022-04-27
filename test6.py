class arithmetic():

    @staticmethod
    def take_square(num1):
        return num1 * num1


r = arithmetic.take_square(5)
print(r)

my_ar = arithmetic()
r2 = my_ar.take_square(5)
print(r2)