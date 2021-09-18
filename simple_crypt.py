# import string
# i=input
# my_dict = {ord(x):ord(y) for y,x in zip(string.ascii_uppercase,i())}
# print(''.join([chr(my_dict[ord(x)]) for x in i()]))

#option 2
# i=input
# a=i()
# print(*[chr(a.index(c)+65)for c in i()],sep='')

#option3
I=input
d=I()
for e in I():print(chr(65+d.index(e)),end="")
