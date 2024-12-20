def calc_mod_inverse(num, mod):
    for i in range(mod):
        if (num * i) % mod == 1:
            return i


my_numbers = [int(x) for x in "432 331 192 108 180 50 231 188 105 51 364 168 344 195 297 342 292 198 448 62 236 342 63".split()]
result = []
for i in my_numbers:
    found_inverse = calc_mod_inverse(i, 41)
    if found_inverse < 27:
        result.append(chr(96+found_inverse))
    elif found_inverse < 37:
        result.append(chr(48+found_inverse-27))
    else:
        result.append("_")

print("".join(result))

