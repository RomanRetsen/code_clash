'''
This challenge is about finding which Student(s) has the *second worst* mark. The input.txt file contains the number of student in
the first line, followed by the name of the first student on the next line, and the mark of the first student. It then
goes through each student alternating lines with names and mark.

For example :
5
Harry
37.21
Berry
37.22
Tina
37.2
Akriti
41
Harsh
39

In this example Harry and Berry are equally the second worst students on the exam.
'''

import math


def read_2_lines(file):
    name = file.readline()
    score = file.readline()
    try:
        if name and score:
            return (name, float(score))
    except:
        return None
    return None


f = open(r"C:\Container\Downloads\input.txt")
f.readline()
counter = 0
worst_score = math.inf
worst_name = None
second_worst_score = math.inf
second_worst_name = None
while not (name_and_score := read_2_lines(f)) is None:
    if name_and_score[1] < second_worst_score:
        if name_and_score[1] < worst_score:
            second_worst_score = worst_score
            second_worst_name = worst_name
            worst_score = name_and_score[1]
            worst_name = name_and_score[0]
        else:
            second_worst_score = name_and_score[1]
            second_worst_name = name_and_score[0]

print(f"Worst student is {worst_name} with score {worst_score}")
print(f"Second worst student is {second_worst_name} with score {second_worst_score}")
f.close()

# TASK FOR FUTURE
# write solution in list. and test efficiency

