'''
Remove globally the lowest letter (in term of ASCII order) in the given string.
Input
Line 1 : A string s
Output
Line 1 : The string without occurrences of the first lowest letter
Constraints
Line 1 : A lower cased string composed of alphabetical and space characters (length < 255)
Example

Input

clash of code

Output

clsh of code

-------------------test2
hello world

output

hello worl
--------------------test3
javascript

output 

jvscript
----------test4
go

output
o

'''

s = input()
lowest = 1000
index = [-1,]
for indx, i in enumerate(s):
    if ord(i) > 96 and ord(i) == lowest:
        index.append(indx)
    elif ord(i) > 96 and ord(i) < lowest:
        index.clear()
        index.append(indx)
        lowest = ord(i)

r = []
for i in range(len(s)):
    if not i in index:
        r.append(s[i])

print("".join(r))

'''
other person much simpler solution. genius

s = input()
x = min([x for x in s if x.isalpha()])
print(s.replace(x,''))
'''