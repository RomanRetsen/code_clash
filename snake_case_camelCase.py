"""
Each programming language has its own conventions.
Your company has just switched from one language that uses snake_case to one using camelCase.
Your boss has tasked you with converting variable names from snake_case to camelCase.

To do this, strip the variable name of all underscores (_) and capitalize the letter after each underscore.
Input
A single line containing the variableName in snake_case.
Output
A single line with the variableName converted to camelCase.
Constraints
The variableName will always be in valid snake_case. It will never be a CONSTANT or contain any uppercase letters.
It can, however, contain numbers.
Example
Input

test_case

Output

testCase

-------------test2
test_2

test2

-------------test3

number_1_in_the_middle

out

number1InTheMiddle

-----------test4

underscore_at_the_end_

out

underscoreAtTheEnd

-----------test5

few____InTheMiddle

out

fewInTheMiddle

--------------test6

__hidden_variable

output

hiddenVariable

"""


import re

variable_name = input()
pattern = r'([A-Za-z0-9]*)(_+)(\w*)'
while (result := re.search(pattern, variable_name)):
    prefix_string = result.group(1)
    if len(result.group(3)) > 1:
        if len(result.group(1)):
            replaced_string = result.group(3)[0].upper() + result.group(3)[1:]
        else:
            replaced_string = result.group(3)[0].lower() + result.group(3)[1:]
    elif len(result.group(3)) == 1:
        if len(result.group(1)):
            replaced_string = result.group(3)[0].upper()
        else:
            replaced_string = result.group(3)[0].lower()
    else:
        replaced_string = ""
    variable_name = re.sub(pattern, f'{prefix_string}{replaced_string}', variable_name)
print(variable_name)