def dec2bin(int_input):
    if int_input <= 2:
        return f'{str("" if int_input//2 == 0 else 1)} {str(int_input%2)}'
    else:
        return f'{str(dec2bin(int_input//2))} {str(int_input%2)}'


print(dec2bin(256))