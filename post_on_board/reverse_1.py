"""
Input
Expected output

####  #      ######  ##

4 1 6 2

02
Test 2
Input
Expected output

   ####  ##     ####   ##  ######  ##   

4 2 4 2 6 2

03
Test 3
Input
Expected output

#

1

04
Test 4
Input
Expected output

   # # # # # #                              ##

1 1 1 1 1 1 2

"""
import re

patter = r'\s?(#+)\s?'

_input = input()

r = re.findall(patter, _input)
print(*[len(x) for x in r])
