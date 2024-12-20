size = int(input())
for level in range(size):
    for star in range(0, level+2):
        print(("*" * (star * 2 + 1)).rjust(((size - star) + (star * 2 + 1)), " "))
print("|".center(size * 2 + 1, " "))
print("V".center(size * 2 + 1, "="))
