n = int(input())
the_dict = {}
for item in range(n):
    type, size, color = input().split()
    if type == "sock":
        if not (the_key := f"{size}@{color}") in the_dict:
            the_dict[the_key] = 1
        else:
            the_dict[the_key] += 1

final_number = 0
unpaired = []
for key, value in the_dict.items():
    if value % 2 == 1:
        unpaired.append(key)
        final_number += 1
print(final_number)
for e in sorted(unpaired, key=lambda x:int(x.split("@")[0])):
    print(*(e.split("@")))