"""
For a given text, give the percentage of each letter in it.
Your answer must be sorted in alphabetic order.
Non-sensitve case.
Input
Text : the text you have to analyse
Output
A line with each char of the text followed by the part of the text it represents
Constraints
0 <= len(text) < 351
Example
Input

hello

Output

e20 h20 l40 o20



----------test2 many spaces

hello     .

e9 h9 l18 o9

----------test3

762acbff-b708-11eb-acbd-000000000000

a5 b11 c5 d2 e2 f5


--------------test4 - one letter

A

a100

"""

text = input().lower()
l = len(text)
final_dir = {x:text.count(x) for x in set(text) if x.isalpha()}
print(*[f'{x[0]}{str(int(x[1]/l*100))}' for x in sorted(final_dir.items(), key=lambda x:x[0])])