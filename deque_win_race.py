from random import randint
import time
import collections

#version 1

my_string = ''.join([str(randint(1,9)) for _ in range(100000)])
string_len = len(my_string)
newform_string = []
str_len = -3
chunk = my_string[str_len:]
t0 = time.time()
while True:
    if len(chunk) == 3:
        newform_string.insert(0, chunk)
        str_len -= 3
        chunk = my_string[str_len:str_len+3]
    elif chunk:
        newform_string.insert(0, chunk)
        break
    else:
        break
print(','.join(newform_string))
t1 = time.time()
#version 2

print(f'The result2 is {int(my_string):,d}')
t2 = time.time()
#version3

newform_version3 = []
for index, i in enumerate(my_string[::-1], 1):
    newform_version3.insert(0, i)
    if index % 3 == 0:
        newform_version3.insert(0, ',')
print(''.join(newform_version3))
t3 = time.time()

correction = string_len // 3 if string_len % 3 == 0 else string_len // 3 + 1
print(f'Correction is {correction}')
my_d = collections.deque(maxlen=string_len + correction)
for index, i in enumerate(my_string[::-1], 1):
    my_d.appendleft(i)
    if index % 3 == 0:
        my_d.appendleft(',')
print('\n deque version \n')
print(''.join(my_d))
t4 = time.time()


print(f'slice version1: {str(t1-t0)}')
print(f'formating version2: {str(t2-t1)}')
print(f'iteration version3: {str(t3-t2)}')
print(f'deque len {len(my_d)}like 3 but with deque version4: {str(t4-t3)}')
