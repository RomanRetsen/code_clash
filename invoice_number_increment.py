import re

#version that fix out of range situation
# def increment_string(value_to_inc, inc):
#     final_number = []
#     for i in value_to_inc[::-1]:
#         value_in = int(i) + inc
#         inc = value_in // 10
#         final_number.append(value_in % 10)
#     while inc > 0 :
#         final_number.append(inc % 10)
#         inc //=10
#     return "".join([str(x) for x in final_number[::-1]])

def increment_string(value_to_inc, inc):
    final_number = []
    for i in value_to_inc[::-1]:
        value_in = int(i) + inc
        inc = value_in // 10
        final_number.append(value_in % 10)
    if inc == 0:
        return "".join([str(x) for x in final_number[::-1]])
    else:
        return "OUTOFRANGE"

template = input()
increment = int(input())
pattern = r'[^\d]*(\d+)$'
result = re.search(pattern, template)
if result:
    value_to_inc = result.group(1)
    new_value = increment_string(value_to_inc, increment)
    if new_value == "OUTOFRANGE":
        print("OUTOFRANGE")
    else:
        print(template.replace(value_to_inc, new_value))
else:
    print("INVALID")
    
# You must output the next invoice number, based on a template and an increment.
#
# The template is a string that must end with a number. If it's possible you must add the increment to this number.
#
# Example:
# template INVOICE-0040
# increment 8
# Output INVOICE-0048
#
# template can be invalid if it doesn't end with a number. In this case output must be INVALID
#
# If the next invoice number has more digits than the template, you must output OUT OF RANGE (e.g. if template is SI-00 and the increment is 100, SI-100 is not a valid answer).
# Input
# First line : a string, the template
# Second Line : an integer, the increment
# Output
# INVALID, OUT OF RANGE or an invoice number.
# Constraints
# 1 < the length of the template < 50
# 1 < increment < 10000
# Example
# Input
#
# INVOICE-0040
# 8
#
# Output
#
# INVOICE-0048
#
#
#
#
# INVOICE-0040
# 8
#
# INVOICE-0048
#
# __________________-----
#
#
#
# INVOICE-0000A
# 16
#
#
# INVALID
#
#
# __________________
#
#
# **MAGIC**001
# 29
#
#
# **MAGIC**030
#
# _______________________
#
# 12345
# 5
#
#
# 12350
#
#
# _______________
#
#
# SI-0040-0040
# 5
#
#
# SI-0040-0045
#
#
# ____________
#
#
#
# INVOICE-0040
# 10000
#
#
#
