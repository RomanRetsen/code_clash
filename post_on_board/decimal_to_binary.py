import math

def dec_to_bin(n):
    result = []
    len_bits = math.log(n, 2)
    if int(len_bits) == len_bits:
        len_bits = int(len_bits) - 1
    else:
        len_bits = int(len_bits)
    for i in range(len_bits, -1, -1):
        # bitwise operation shift can be replaced by andmask = 2 ** i
        andmask = 1 << i
        r = n & andmask
        result.append("0") if r == 0 else result.append("1")
    return f"0b{''.join(result)}"

the_number = int(input())
print(dec_to_bin(the_number))

