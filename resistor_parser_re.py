import re
import collections


resistor = f'(?P<RES>\w+)\s*'
lparen   = f'(?P<LPAREM>\()'
rparen   = f'(?P<RPAREM>\))'
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

resistors = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    name = inputs[0]
    r = int(inputs[1])
    resistors[name] = r

circuit = input()

for tok in generate_tokens(circuit):
    print(tok)

