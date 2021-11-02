import re

my_string = "a123bc34d8ef34"


def my_func(in_str):
    tmp = (set(re.sub(r"[a-z]", " ", in_str).strip().split()))
    return tmp

print(my_func(my_string))