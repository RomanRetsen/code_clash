with open(r"C:\Container\Downloads\3b.txt") as f:
    fizz = 0
    buzz = 0
    fizz_buzz = 0
    for line in f:
        number = int(line.strip())
        if not number % 3:
            fizz += 1
            if not number % 5:
                fizz_buzz += 1
        if not number % 5:
            buzz += 1
            if not number % 3:
                fizz_buzz += 1

print(fizz, buzz, fizz_buzz)
print(sum((fizz, buzz, fizz_buzz)))
