'''
The Simple BF language consists of three characters and a single 8-bit value in memory.
+ indicates to increment that value.
- decrements it.
. means output the current ASCII value.

This value cannot underflow or overflow.
If the memory value would become negative, value < 0, output UNDERFLOW.
If the memory value would exceed 8-bit, value > 255, output OVERFLOW.
The value starts at 0.
Input
A string only consisting of characters + - .
Output
The output string of the program if the memory stays within bounds.
Otherwise UNDERFLOW or OVERFLOW.
Constraints
0 < input length < 1024
0 <= memory value < 256
Example
Input

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++.-----------.+.-----------------------.

Output

CODE.
----------------

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

output
OVERFLOW

----------------------


+.--.

UNDERFLOW

---------------------------


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.---.+++++++++.---------------------------------------...++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.------------------------------------------------------------.-----.+++.--.

SPY222p4/20

----------------------

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.

d

'''

s = input()[:-1].split(".")
memory = 0
final_print = []
for ch in s:
    memory += sum([1 if x == "+" else -1 if x == "-" else 1000000 for x in ch])
    if memory > 255:
        print("OVERFLOW")
        break
    elif memory < 0:
        print("UNDERFLOW")
        break
    else:
        final_print.append(chr(memory))
else:
    print("".join(final_print))
