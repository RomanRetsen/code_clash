import random

# get a string from user and find if word sleep in it
# somevar = input()
# if "sleep" in somevar:
#     print("The word 'sleep' IS in the sentence")
# else:
#     print("The word 'sleep' IS NOT in the sentence")
#

# user_number = int(input())
#
# if user_number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")

# def another_game_func():
#     user_choice = input("Another game?(y/n) ")
#     if user_choice == "n":
#         return 0
#     else:
#         return random.randint(1, 80)
#
# nom = random.randint(1, 80)
# counter = 1
# while True:
#     user_guess = int(input("Guess the number between 1 and 80: "))
#     if user_guess == nom:
#         print(f"You got it!!! You've managed to guess the number in {counter} times")
#         another_game = another_game_func()
#         if another_game == 0:
#             break
#         else:
#             nom = another_game
#             counter = 1
#             continue
#     elif user_guess < nom:
#         print("go higher")
#         counter += 1
#     elif user_guess > nom:
#         print("secret number is smaller")
#         counter += 1

# s = "this ends here"
# list_from_s = s.split()
# print(" ".join(list_from_s))
# print("".join(list_from_s))

# my_list = ["name", "one"]
# my_list.append("2")
# my_list.insert(0, "three")
# print(my_list)

#long version
# def my_func2(input_list):
#     longest_word = ""
#     for word in input_list:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word
#
# #short version
# def my_func(input_list):
#     return sorted(input_list, key=lambda x:len(x))[-1]
#
# temp_list = []
# while True:
#     user_input = input("Enter the word (OR 'no' to exit)>> ")
#     if not user_input == "no":
#         temp_list.append(user_input)
#     else:
#         print(f"{my_func(temp_list)} is the longest word in the list")
#         break
# ls = []
# while user_inputed_word := input("Enter something SVP:>> "):
#     ls.append(user_inputed_word)
#
# print(ls)

# for line in open("log.txt"):
#     temp_list = line.split()
#     if temp_list[-2] == "404":
#         print(f"IP with 404 error is {temp_list[0]}")

# [print(x.strip().split()[0]) for x in open("log.txt") if x.strip().split()[-2] == "404"]

# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print("YesNo")
# elif num % 3 == 0:
#     print("Yes")
# elif num % 5 == 0:
#     print("No")
# else:
#     print("Neither")

# for y in range(1, 30):
#     print(y)

# print(*["yesno" if x % 3 == 0 and x % 5 ==0
#        else "yes" if x % 3 == 0
#        else "no" if x % 5 == 0
#        else x for x in range(1, 31)])

fruit_list = []
while fruit := input("Enter fruit>> "):
    fruit_list.append(fruit)
else:
    print(fruit_list)

