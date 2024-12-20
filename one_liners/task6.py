my_str = "cvpbPGS{P7e1S_54I35_71Z3}"
print(len(my_str))

result  = "".join([chr((ord(x)-65+13)%26+65) if ord(x) > 64 and ord(x) < 91 \
                   else chr((ord(x)-97+13)%26+97) if ord(x) > 96 and ord(x) < 123 \
                   # else chr((ord(x)-48+13)%10+48) if ord(x) > 47 and ord(x) < 58 \
                   else x if ord(x) > 47 and ord(x) < 58 \
                   else "{" if ord(x) == 123 \
                   else "}" if ord(x) == 125 \
                   else "_" if ord(x) == 95 \
                   else "" for x in my_str])
print(result)
