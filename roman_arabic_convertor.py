import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
converter = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
converter_counter = {1000:0, 900:0, 500:0, 400:0, 100:0, 90:0, 50:0, 40:0, 10:0, 9:0, 5:0, 4:0, 1:0}

n = int(input())

for key, value in converter.items():
    while n >= key:
        n -= key
        print(value, end="")

# for i in converter_counter.items():
#     converter_counter[i[0]] += n // i[0]
#     n = n % i[0]
#
# for key, value in converter_counter.items():
#     print(converter[key] * value, end="" )