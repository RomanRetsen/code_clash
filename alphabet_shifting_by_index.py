l = input()
r = []
for index, i in enumerate(l):
    r.append(chr((ord(i)-96 + index)%26 + 96))

print("".join(r))


# codingamey
#
# cpflrlgtmh
#
# 02
# Test 2
# Input
# Expected output
#
# abcdef
#
# acegik
#
# 03
# Test 3
# Input
# Expected output
#
# cracker
#
# cscfojx
#
# 04
# Test 4
# Input
# Expected output
#
# aaaaaa
#
# abcdef
#
#
#
#
#