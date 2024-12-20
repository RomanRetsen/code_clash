"""

 Goal
Calculate the equivalent resistance of a circuit containing only resistors.

A resistor is a component used in electrical circuits. A resistor is quantified by its Resistance, which is measured in Ohms. We are interested in knowing the total resistance of a circuit of only resistors. There are two key definitions needed to determine the resistance of multiple resistors.

1. Series

The resistance of resistors in a line is equivalent to the sum of the resistance of those resistors.

    ---[R_1]---[R_2]---


Resistors in series will be noted with parentheses ( R_1 R_2 R_3 ... and so on ).

The resistance of a series arrangement is: R_eq = R_1 + R_2 + R_3 + ... and so on, where R_eq is the equivalent resistance of the series arrangement.

2. Parallel

The resistance of resistors in branching paths of the circuit is equal to 1 over the sum of 1 over the resistance of each branching path.

       +---[R_1]---+
       |           |
    ---+           +---
       |           |
       +---[R_2]---+



Resistors in parallel will be noted with brackets [ R_1 R_2 R_3 ... and so on ].

The resistance of resistors in parallel is R_eq = 1/(1/R_1 + 1/R_2 + 1/R_3 + 1/... and so on).

A branch can be treated as a single resistor by determining its equivalent resistance.

Example:

N = 3

A 24
B 8
C 48
[ ( A B ) [ C A ] ]


This will look something like this:

       +---[C]---+
       |         |
    +--+         +--+
    |  |         |  |
    |  +---[A]---+  |
    |               |
    +---[A]---[B]---+
    |               |
    +---[Battery]---+


[ ( A B ) [ C A ] ] => [ 24+8 1/(1/48+1/24) ] => [ 32 16 ] => 1/(1/32+1/16) => 32/3 => 10.666... => 10.7
Input
Line 1: An integer N for the number of unique resistors present in the circuit
Next N lines: A space separated name and the integer resistance R of a resistor
Last line: A space separated combination of parentheses, brackets, and names of resistors
Output
The equivalent resistance expressed as a float rounded to the nearest 0.1 Ohms.
Constraints
0 < N < 10
0 < R < 100
Example
Input

2
A 20
B 10
( A B )

Output

30.0
---------------test2 paralel
2
C 20
D 25
[ C D ]

out
11.1
------------test3 combined

3
A 24
B 8
C 48
[ ( A B ) [ C A ] ]

out

10.7

----------test4 complex

7
Alfa 1
Bravo 1
Charlie 12
Delta 4
Echo 2
Foxtrot 10
Golf 8
( Alfa [ Charlie Delta ( Bravo [ Echo ( Foxtrot Golf ) ] ) ] )

out

2.4

-----------test more complex

1
Star 78
[ ( [ Star ( Star Star ) ] [ Star ( Star Star ) ] Star ) ( [ Star ( Star Star ) ] [ Star ( Star Star ) ] Star ) ]

out

91.0

"""
import re
import collections


resistor = f'(?P<RES>\w+)\s*'
lparen   = f'(?P<LPAREN>\()'
rparen   = f'(?P<RPAREN>\))'
lbracet  = f'(?P<LBRACET>\[)'
rbracet  = f'(?P<RBRACET>\])'
white_space       = r'(?P<WS>\s+)'

resist_pattern = re.compile("|".join([resistor, lparen, rparen, lbracet, rbracet, white_space]))
Token = collections.namedtuple("Token", ["type", "value"])

def generate_tokens(input_seqence):
    scanner = resist_pattern.scanner(input_seqence)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group().strip())
        if tok.type != "WS":
            yield tok


levels = {}
resistors = {}
current_level = []
n = int(input())
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    resistors[name] = r

circuit = input()

def add_resistor(value):
    lvl = None
    for level in current_level:
        if lvl is None:
            lvl = levels[level]
        else:
            lvl = lvl[level]
    if "VALUE" in lvl:
        lvl["VALUE"].append(resistors[value])
    else:
        lvl["VALUE"] = [resistors[value],]

def create_level(level_to_add):
    lvl = None
    for level in current_level:
        if lvl is None:
            lvl = levels[level]
        else:
            lvl = lvl[level]
    if lvl is None:
        levels[level_to_add] = {}
    else:
        lvl[level_to_add] = {}

def resolve_level(operation):
    lvl = None
    for level in current_level:
        if lvl is None:
            prev_level = levels
            lvl = levels[level]
        else:
            prev_level = lvl
            lvl = lvl[level]

    if operation == "series":
        resolved_value = round(float(sum(lvl["VALUE"])), 1)
        prev_level.pop(operation)
        # prev_level["VALUE"] = resolved_value
        if "VALUE" in prev_level:
            prev_level["VALUE"].append(resolved_value)
        else:
            prev_level["VALUE"] = [resolved_value,]
    elif operation == "paralel":
        resolved_value = round(1 / sum([1/x for x in lvl["VALUE"]]), 1)
        prev_level.pop(operation)
        # prev_level["VALUE"] = resolved_value

        if "VALUE" in prev_level:
            prev_level["VALUE"].append(resolved_value)
        else:
            prev_level["VALUE"] = [resolved_value,]


for tok in generate_tokens(circuit):
    if tok.type == "LPAREN":
        create_level("series")
        current_level.append("series")
    elif tok.type == "RPAREN":
        resolve_level("series")
        if current_level[-1] == "series":
            current_level.pop()
    elif tok.type == "LBRACET":
        create_level("paralel")
        current_level.append("paralel")
    elif tok.type == "RBRACET":
        resolve_level("paralel")
        if current_level[-1] == "paralel":
            current_level.pop()
    elif tok.type == "RES":
        add_resistor(tok.value)
print(levels["VALUE"][0])

"""
#other guy solution

def series(*args):
    return sum(map(float, args))

def parallel(*args):
    return 1/sum(1/float(arg) for arg in args)


R = dict()
for _ in range(int(input())):
    name, r = input().split()
    R[name] = r

circuit = (input().replace(' ', ',')
            .replace('(,', 'series(')
            .replace('[,', 'parallel(')
            .replace(']', ')')
)

for key in R:
    circuit = circuit.replace(key, R[key])

print(f'{eval(circuit):.1f}')
"""

#person 2 solution

"""
def do_split(line):
    result = []
    stack = []
    prev_index = 0
    for index in range(len(line)):
        if line[index] in "[(":
            stack.append(line[index])
        elif line[index] in "])":
            stack.pop()
        if len(stack) == 0:
            result.append(line[prev_index:index+1])
            prev_index = index+1
    return result

def calc(circuit):
    if circuit[0] == "[" and circuit[-1] == "]":
        split_result = do_split(circuit[1:-1])
        result = 1/(sum(map(lambda x: 1/calc(x), split_result)))
        return result
    
    if circuit[0] == "(" and circuit[-1] == ")":
        split_result = do_split(circuit[1:-1])
        result = sum(map(calc, split_result))
        return result
    
    return resistors[circuit[0]]


n = int(input())
resistors = dict()
for i in range(n):
    inputs = input().split()
    resistors[inputs[0]] = int(inputs[1])
source_circuit = input().split(" ")

print("%.1f" % calc(source_circuit))
"""