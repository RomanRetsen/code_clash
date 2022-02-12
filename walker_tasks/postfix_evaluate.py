'''
Don’t worry, we will x it in the post
def postfix_evaluate(items):
When arithmetic expressions are given in the familiar in ix notation 2 + 3 * 4, parentheses nudge
the different evaluation order to differ from the usual PEMDAS order determined by precedence
and associativity of each operator. The alternative post ix notation (also known as Reverse Polish
Notation, for all you “simple Poles on a complex plane”) may irst look weird to people accustomed
to the conventional in ix. However, post ix notation turns out to be easier for machines, since it
allows encoding any intended evaluation order without any parentheses!
A post ix expression is given as a list of items that can be either individual integers, or one of the
strings '+', '-', '*' and '/' to denote the four basic arithmetic operators. To evaluate a post ix
expression using a simple linear loop, use an ordinary list as an initially empty stack. Loop through
the items one by one, from left to right. Whenever the current item is an integer, just append it to
the end of the list. Whenever the current item is one of the four arithmetic operations, pop two
items from the end of the list to perform that operation on, and append the result back to the list.
Assuming that items is a legal post ix expression, which is guaranteed in this problem so that you
don't need to perform any error detection or recovery, once all items have been processed, the lone
number left in the stack becomes the inal answer.
To avoid the intricacies of loating point arithmetic, you should perform the division operation using
the Python integer division operator // that truncates the result to the integer part. Furthermore,
to avoid the crash from dividing by zero, this problem comes with an arti icial (yet mathematically
perfectly sound) rule that division by zero gives a zero result, instead of crashing.
items (equivalent in ix) Expected result
[2, 3, '+', 4, '*'] (2+3) * 4 20
[2, 3, 4, '*', '+'] 2 + (3*4) 14
[3, 3, 3, '-', '/', 42, '+'] 3 / (3 - 3) + 42 42
[7, 3, '/'] 7 / 3 2
[1, 2, 3, 4, 5, 6, '*', '*', '*',
'*', '*'] 1 * 2 * 3 * 4 * 5 * 6 720
(By adding more operators and another auxiliary stack, an entire Turing-complete programming
language can be built around post ix evaluation. Interested students can sally forth to the Wikipedia
page "Forth" to learn more of this ingeniously simple concatenative programming language.)
'''
import operator

def postfix_evaluate(items):
    operational_stack = []
    operations = {"+":operator.add, "-":operator.sub, \
                  "/":operator.floordiv, "*":operator.mul
                  }
    for item in items:
        if item in operations:
            operand_2 = operational_stack.pop()
            operand_1 = operational_stack.pop()
            if item == "/" and operand_2 == 0:
                return 0
            operational_stack.append(
                operations[item](operand_1, operand_2)
            )
        elif str(item).isdigit():
            operational_stack.append(item)
    if len(operational_stack) == 1: # it could be only one left-over item in the list
        return operational_stack[0]
    else:
        return 0

# input_data = [2, 3, '+', 4, '*'] # (2+3) * 4  # result 20
# input_data = [2, 3, 4, '*', '+']  # 2 + (3*4) result 14
# input_data =  [3, 3, 3, '-', '/', 42, '+'] # 3 / (3 - 3) + 42 result  42
# input_data = [7, 3, '/'] # 7 / 3  result 2
# input_data =  [1, 2, 3, 4, 5, 6, '*', '*', '*', '*', '*'] # 1 * 2 * 3 * 4 * 5 * 6 result 720
# input_data = [10, 9, "/"]
# input_data = [int(x) if x.isdigit() else x for x in "10 3 5 * 16 4 - / +".split(" ")]
input_data = []

print(postfix_evaluate(input_data))
