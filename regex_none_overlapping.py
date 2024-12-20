import re


# lookahead assertion used to reach non-overlapping search
pattern = r"(?=nn)"
# pattern = r"nn"
the_str = "startnnnaaannend"
marker = 0
result_list = []

for i in re.finditer(pattern, the_str):
    print(i.span()[0])
    result_list.append(the_str[marker:i.span()[0]])
    result_list.append("*")
    marker = i.span()[0] + 2
else:
    result_list.append(the_str[marker:])

print("".join(result_list))