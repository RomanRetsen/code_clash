"""
Write a program that takes a string S and, for each character prints the following response:
- If the character is an upper-case letter [A-Z] then first print out all the upper-case letters before it. (For example 'C' --> 'ABC', 'E'-->'ABCDE', etc).
- If the character is a lower-case letter [a-z] then first print out all the lower-case letters before it.
- If the character is a digit [0-9], then first print out all the digits before it, starting from 0.
Input
One line: a string S containing alphanumerical characters.
Output
One line: a string containing each character of S, preceeded with the right characters as stated above.
Constraints
- S will be between 0 and 255 characters (inclusive)
- S will only contain alphanumeric characters
Example
Input

B

Output

AB

--------test2

d

abcd

----------test3

5


012345


----------test4

Bd5


ABabcd012345

----------test5

Zz9



ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789


------------------------
"""


import string

def the_func(n):
    if n in "0123456789":
        return "".join([chr(48+x) for x in range(ord(n) - 48)])
    elif n in string.ascii_lowercase:
        return "".join([chr(97+x) for x in range(ord(n) - 97)])
    elif n in string.ascii_uppercase:
        return "".join([chr(65+x) for x in range(ord(n) - 65)])

s = input()

print("".join([f'{the_func(x)}{x}' for x in s]))