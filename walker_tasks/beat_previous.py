'''
Beat the previous
def extract_increasing(digits):
Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create
and return the list of increasing integers acquired from reading these digits in order from left to
right. The irst integer in the result list is made up from the irst digit of the string. After that, each
element is an integer that consists of as many following consecutive digits as are needed to make
that integer strictly larger than the previous integer. The leftover digits at the end of the digit string
that do not form a suf iciently large integer are ignored.
digits Expected result
'600005' [6]
'045349' [0, 4, 5, 34]
'77777777777777777777777' [7, 77, 777, 7777, 77777, 777777]
'122333444455555666666' [1, 2, 23, 33, 44, 445, 555, 566,
666]
'2718281828459045235360287
47135266249775724709369995
95749669676277240766303535
47594571382178525166427427
46639193200305992181741359
6629043572900334295260' [2, 7, 18, 28, 182, 845, 904,
5235, 36028, 74713, 526624,
977572, 4709369, 9959574,
96696762, 772407663, 3535475945,
7138217852, 51664274274,
66391932003, 599218174135,
966290435729]
'1234' * 100 A list with 38 elements, the last one equal to
341234123412341234123
'420' * 420 A list with 56 elements, the last one equal to
420420420420420420420420420420420
420420420
'''
the_string = input()
# the_string = '420' * 420

current = int(the_string[0])
result = [current,]
build = 0
build_string = []
for char in the_string[1:]:
    build_string.append(char)
    build = int("".join(build_string))
    print(build)
    if build > current:
        result.append(build)
        current = build
        build = 0
        build_string.clear()

print(result)