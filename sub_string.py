"""
Task
You are given a string .
Your task is to find the indices of the start and end of string in

.

Input Format

The first line contains the string
.
The second line contains the string

.

Constraints


Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa

Sample Output

(0, 1)  
(1, 2)
(4, 5)

"""
# in_string = input()
# sub_string = input()
#
# current_index = in_string.find(sub_string)
# if not current_index == -1:
#     while not in_string.find(sub_string, current_index) == -1:
#         find_index = in_string.find(sub_string, current_index)
#         print((find_index, find_index + len(sub_string)-1))
#         current_index = find_index + 1
# else:
#     print((-1, -1))

import re

in_string = "aasdfmapljjtjkapap"
sub_patter = r".ap"
off_set = 0
current_index = re.search(sub_patter, in_string)

if current_index:
    while current_index:
        print((current_index.start() + off_set, current_index.end() + off_set - 1))
        off_set += current_index.start() + 1
        current_index = re.search(sub_patter, in_string[off_set:])
else:
    print((-1, -1))
