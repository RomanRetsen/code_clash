# if entered.isdigit():
#     entered_number = int(entered)
#     print(f"Entered interger is {entered_number}")
# elif entered.replace(".", "", 1).isdigit():
#     entered_number = float(entered)
#     print(f"Entered float is {entered_number}")
# else:
#     print(f"its neither int no float")

# def whatisit(entered_value):
#     try:
#         converted_float_value = float(entered_value)
#         converted_int_value = int(converted_float_value)
#     except ValueError:
#         return "string"
#     else:
#         if converted_float_value == converted_int_value:
#             return "int"
#         else:
#             return "float"

def whatisit(entered_value):
    try:
        converted_float_value = float(entered_value)
        if converted_float_value % 1 == 0:
            return "int"
        else:
            return "float"
    except ValueError:
        return "str"
print(whatisit(input()))