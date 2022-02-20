'''


7
8
3
4

#######
#     #
# ### #
# # # #
# # # #
# ### #
#     #
#######

02
Test 2
Input
Expected output

10
8
8
4

##########
#        #
##########
##      ##
##      ##
##########
#        #
##########

03
Test 3
Input
Expected output

10
6
8
4

##########
##########
##      ##
##      ##
##########
##########

04
Test 4
Input
Expected output

10
14
4
8

##########
#        #
#        #
#  ####  #
#  #  #  #
#  #  #  #
#  #  #  #
#  #  #  #
#  #  #  #
#  #  #  #
#  ####  #
#        #
#        #
##########


'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

b_b = (b - d) // 2
a_a = (a - c) // 2
print(b_b)
print("#" * a)
for i in range(1, b - 1):
    if i < b_b or i >= (b_b + d ) :
        print("#", " " * (a - 2), "#", sep="")
    elif i == b_b or i == (b_b + d - 1):
        print("#", f"{'#' * c}".center(a - 2, " "), "#", sep="")
    else:
        print("#", f"#{' ' * (c - 2)}#".center(a - 2, " "), "#", sep="")
print("#" * a)