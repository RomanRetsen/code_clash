import random



# mean
# the_list2 = [10,23,10,19,21,23,21,17, 20.2]
#
# the_list2_s = (sorted(the_list2))
#
# print(f"Sorted {the_list2_s}")
# if len(the_list2_s) % 2 == 0:
#     print(sum(the_list2_s[len(the_list2_s)//2-1:len(the_list2_s)//2+1]) // 2)
# else:
#     print(the_list2_s[len(the_list2_s)//2])

the_list = [random.randint(1, 100) for _  in range(20)]

print(the_list)

the_list[2:4] = [1000,2000, 3000]
print(the_list)

