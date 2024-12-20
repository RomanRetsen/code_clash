'''
Given an input file containing a series of characters of either “(“ or “)”.
The first character raise the elevator of 1 floor up, and the second lowers it by 1 floor,
identify what is the ending floor after the whole sequence.
'''

f = open(f"C:\Container\Downloads\s3_e2b.txt")
line = f.readline()
up = line.count("(")
down = line.count(")")
print(up - down)
f.close()