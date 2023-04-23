file1 = []
file2 = []


with open("file11") as f:
    for line in f:
        for word in line.strip().split():
            file1.append(word)
with open("file22") as f:
    for line in f:
        for word in line.strip().split():
            file2.append(word)

file1_set = set(file1)
file2_set = set(file2)
print(file2_set.difference(file1_set))
