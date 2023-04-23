import string


counters = {x:0 for x in string.ascii_letters}

print(counters)

with open("IADB.txt") as f:
    for line in f:
        for letter in line:
            if letter in counters:
                counters[letter] += 1

my_min = min([counters["I"],counters["A"], counters["D"], counters["B"]])
print(my_min)

counters_fixed = {x:counters[x] for x in counters if not counters[x] == 0}

parts = []
for i in string.ascii_uppercase:
    if i in counters_fixed:
        parts.append(f"{i}={counters_fixed[i]}")
for i in string.ascii_lowercase:
    if i in counters_fixed:
        parts.append(f"{i}={counters_fixed[i]}")

parts.append(f"IADB={my_min}")
print(",".join(parts))

