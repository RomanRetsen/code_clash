import operator

def infix_to_postfix(infix_expr):
    op_stack = []
    result = []
    operators = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

    for element in infix_expr.split():
        if element == "(":
            op_stack.append("(")
        elif element == ")":
            while not (e := op_stack.pop()) == "(":
                result.append(e)
        elif element not in operators:
            result.append(element)
        elif element in operators:
            while len(op_stack) > 0 and operators[op_stack[-1]] >= operators[element]:
                result.append(op_stack.pop())
            op_stack.append(element)
        print(op_stack)
    else:
        while len(op_stack) > 0:
            result.append(op_stack.pop())
    return " ".join(result)

def postfix_to_result(postfix_expr):
    op_stack = []
    operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

    for element in postfix_expr.split():
        if element in operators:
            op_stack.append(operators[element](float(op_stack.pop()), float(op_stack.pop())))
        else:
            op_stack.append(element)
    return op_stack[0]

# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("A * ( B + C ) * D"))
# print(infix_to_postfix("( A + ( B + ( C + D ) ) ) * E"))
print(postfix_to_result(infix_to_postfix("( 1 + ( 4 + ( 2 + 7 ) ) ) * 10")))
print(postfix_to_result(infix_to_postfix("1 + 4 + 2 + 7 * 10")))
print(eval("( 1 + ( 4 + ( 2 + 7 ) ) ) * 10"))
