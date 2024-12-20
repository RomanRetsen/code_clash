"""
You are given a 1-dimensional spreadsheet. You are to resolve the formulae and give the value of all its cells.

Each input cell's content is provided as an operation with two operands arg1 and arg2.

There are 4 types of operations:
VALUE arg1 arg2: The cell's value is arg1, (arg2 is not used and will be "_" to aid parsing).
ADD arg1 arg2: The cell's value is arg1 + arg2.
SUB arg1 arg2: The cell's value is arg1 - arg2.
MULT arg1 arg2: The cell's value is arg1 × arg2.

Arguments can be of two types:
• Reference $ref: If an argument starts with a dollar sign, it is a interpreted as a reference and its value is equal to the value of the cell by that number ref, 0-indexed.
For example, "$0" will have the value of the result of the first cell.
Note that a cell can reference a cell after itself!

• Value val: If an argument is a pure number, its value is val.
For example: "3" will have the value 3.

There won't be any cyclic references: a cell that reference itself or a cell that references it, directly or indirectly.
Input
Line 1: An integer N for the number of cells.
Next N lines: operation arg1 arg2

operation is one of { VALUE, ADD, SUB, MULT }
arg1 and arg2 are either a number ("-?[0-9]+"), a reference ("\$[0-9]+") or nothing "_".
Output
N lines: the value of each cell, one value per line, from cell 0 to cell N
Constraints
1 ≤ N ≤ 100
-10000 ≤ val ≤ 10000
$0 ≤ $ref ≤ $(N-1)
val ∈ ℤ
ref ∈ ℕ
There are no cyclic references.

Example ------- simple dependency
Input

2
VALUE 3 _
ADD $0 4

Output

3
7
-------------test 2 Double dependency
3
VALUE 20 _
ADD $0 100
ADD $1 1

out

20
120
121

-------------test 3 No dependencies 

3
ADD 1 2
SUB 3 1
MULT 2 4

out

3
2
8

----------- test 4 Fibonacci

9
VALUE 0 _
VALUE 1 _
ADD $0 $1
ADD $1 $2
ADD $2 $3
ADD $3 $4
ADD $4 $5
ADD $5 $6
ADD $6 $7

out 

0
1
1
2
3
5
8
13
21

-------test 5 Backward dependency

2
ADD $1 20
VALUE 32 _

out

52
32
--------test 6 Hard

100
SUB $47 $9
SUB 44 $59
ADD $97 $67
ADD $1 $1
SUB $57 $67
ADD $47 $97
ADD $59 $59
SUB $50 $83
SUB $3 $93
SUB $4 $74
SUB $38 $0
ADD $29 $96
SUB $46 $97
SUB $5 $98
SUB $87 $66
SUB $86 $25
SUB $1 $98
SUB $84 $56
ADD $38 $78
ADD $46 $34
ADD $5 $76
SUB $3 $93
ADD $19 $31
ADD $97 $77
VALUE $54 _
SUB $6 $6
ADD $98 $2
ADD $59 $67
SUB $36 $86
SUB $98 $26
SUB $16 $7
VALUE $67 _
ADD $11 $84
VALUE $63 _
ADD $3 $6
VALUE $44 _
SUB $68 $5
ADD $7 $58
ADD $50 $82
ADD $88 -936
ADD $43 $47
ADD $58 842
SUB $80 $46
SUB $33 $96
SUB $43 $46
ADD $2 $8
ADD $59 $9
VALUE $2 _
SUB $65 $30
ADD 135 $65
ADD $71 $93
ADD $96 $67
ADD $6 $38
SUB $5 $8
SUB $67 $1
ADD $4 $71
VALUE $67 _
SUB $93 $54
SUB $51 $3
ADD 993 -871
ADD $6 $6
SUB $71 $65
ADD $25 $60
VALUE $59 _
ADD $6 $51
SUB $63 $97
VALUE $67 _
SUB 3 $59
ADD $88 $3
SUB $83 $53
SUB $50 $49
ADD $60 865
VALUE $53 _
SUB $29 $44
SUB $96 $25
ADD $21 $77
SUB $14 $30
SUB $27 $50
ADD $51 $5
SUB $40 $72
VALUE $90 _
ADD $87 $42
ADD $9 $47
SUB $97 $1
ADD $21 $44
ADD $78 $94
ADD $21 $71
ADD -730 $67
SUB $21 $89
SUB $83 $25
ADD $47 $84
ADD $6 $65
ADD $32 $22
ADD $27 $59
ADD $63 $11
ADD $65 $60
ADD $59 $6
SUB $1 $27
ADD $27 $83
SUB $19 $61


out

-119
-78
-200
-156
285
-281
244
1481
-281
-81
1316
566
122
-281
-730
1072
-78
-447
1163
129
548
-281
10
-1556
-41
0
-200
3
-1225
200
-1559
-119
0
122
88
-285
-153
1884
1197
-1214
-444
1245
-807
-244
-285
-481
41
-200
1762
338
1478
247
1441
0
-41
1638
-119
166
403
122
488
1150
488
122
491
203
-119
-119
-434
-3
1140
1353
0
485
366
-1756
829
-1475
-34
-444
-766
-1656
-281
-3
-566
654
1072
-849
-278
-3
-766
447
10
125
688
691
366
-81
0
-1021

"""

class Cell:
    # default constructor for cell with resolved value
    def __init__(self, value, value_type=0, operation="VALUE", operand1="_", operand2="_"):
        self.value = value
        self.value_type = value_type
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2

    def resolve(self):
        if self.operation == "ADD":
            self.value = int(self.operand1) + int(self.operand2)
        elif self.operation == "MULT":
            self.value = int(self.operand1) * int(self.operand2)
        elif self.operation == "SUB":
            self.value = int(self.operand1) - int(self.operand2)
        elif self.operation == "VALUE":
            self.value = int(self.operand1)
        self.value_type = 0

# the engine - recursive function.
def resolve_number(the_sequence, x):
    if the_sequence[x].value is None:
        if the_sequence[x].operand1.startswith("$"):
            the_sequence[x].operand1 = resolve_number(the_sequence, int(the_sequence[x].operand1[1:]))
        if not the_sequence[x].operation == "VALUE" and  the_sequence[x].operand2.startswith("$"):
            the_sequence[x].operand2 = resolve_number(the_sequence, int(the_sequence[x].operand2[1:]))

        the_sequence[x].resolve()
        return the_sequence[x].value
    else:
        return the_sequence[x].value

n = int(input())
the_sequence = [0]*n

for i in range(n):
    operation, arg_1, arg_2 = input().split()

    # VALUE could be either final number (value_type=0)
    # or link to another cell(value_type=1) that must be resolved later.
    if operation == "VALUE" and not arg_1.startswith("$"):
        the_sequence[i] = Cell(value=arg_1)
    elif operation == "VALUE" and arg_1.startswith("$"):
        the_sequence[i] = Cell(value=None, value_type=1, operand1=arg_1)
    elif operation in ["ADD", "MULT", "SUB"]:
        the_sequence[i] = Cell(
                            value=None,
                            value_type=1,
                            operation=operation,
                            operand1=arg_1,
                            operand2=arg_2
                            )

for i in range(n):
    resolve_number(the_sequence, i)
    print(the_sequence[i].value)
