# number = input()
# try:
#     b = 5 + int(number)
#     print(b)
# except ValueError as ve:
#     print("error converting to int")

# my_list = list(range(10))
# my_list.append(10)
# my_list.append(11)
# print(my_list)

# name = input("Enter your name: ")
# age = int(input("Enter your age (integer character only)"))
# if age >= 18:
#     print("You are hired, " + name)
# else:
#     print("You are too young to work, " + name)

# list_of_numbers = []
# a = int(input("Enter 1-st number: "))
# b = int(input("Enter 2-d number"))
# c = int(input("Enter 3-d number"))
# list_of_numbers.append(a)
# list_of_numbers.append(b)
# list_of_numbers.append(c)
# mn, *md, mx = sorted(list_of_numbers)
# print("Smaller number: " + str(mn))
# print("Larger number: " + str(mx))

# names_database = ["Roman","Tony","Alex","Benson","Nigel"]
# new_name = input("Enter your name: ")
#
# if new_name in names_database:
#     print("You are already on the list, " + new_name)
# else:
#     print("You were added to the list, " + new_name)


# temp_list = []
# while True:
#     user_input = input("Enter the word (OR 'no' to exit)>> ")
#     temp_list.append(user_input) if not user_input == "no" else temp_list.append("1")

# temp_list = []
# while True:
#     user_input = input("Enter the word (OR 'no' to exit)>> ")
#     if not user_input == "no":
#         temp_list.append(user_input)
#     else:
#         print(*temp_list)
#         break

# my_int = 5
# my_list = [1,2,3]
#
# def func(input_int, input_list):
#     input_int = 10
#     input_list[0] = 100
#
# func(my_int, my_list)
# print(my_int)
# print(my_list)