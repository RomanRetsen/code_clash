# class Person:
#     def __init__(self, value):
#         self.name = value
#
#     def running(self):
#         print("im runnig")
#
#     def __str__(self):
#         return f"Person with name {self.name}"
#
# g = Person("sasi")
# k = Person("james")
# print(g.name)
# g.running()

# def something(marks):
#     for mark in marks:
#         print(mark)
#         if mark == 56:
#             break
#     else:
#         print("else ")
#     print("Out of loop but still in the function")
# something([1,2,4,56,7,8,9])

# def avg(marks):
#     return  sum(marks)/len(marks)
# 
# print(avg([12,34, 56, 78, 54]))

import random, os
def clear():
    os.system('clear')

def fishing():
    caught = 0
    print("Fishing game!")
    while True:
        clear()
        input("Press enter to cast a line...")
        while True:
            fish = random.randrange(0,5)
            catch = random.randrange(0,5)
            print("Your hook is in the water and you are waiting...")
            if fish == catch:
                print("You caught a fish!")
                input("Press Enter to reel it in!")
                caught += 1
                print(caught)
            else:
                print("You haven't caught a fish yet...")
                KeepFishing = input("Do you want to keep waiting or reel your line back in? (E) for wait and (Q) for reel. : ")
                if KeepFishing.upper() == "Q":
                    print("Okay")
                    break
        CastAgain = str(input("Do you want to cast again or are you done for the day? (E) to cast and (Q) to exit : " ))
        if CastAgain.upper() == "Q":
            print("Okay! Today you caught : ",caught," fish!")
            return caught
number = 0
while True:
    clear()
    print ("Welcome to the fishing program!")
    print ("Currently, you have caught ",number,"fish.")
    Game=str(input("Press E to fish and press Q to exit "))
    clear()
    if Game.upper() == "E":
        number = fishing()
    elif Game.upper() == "Q":
        exit()
    else:
        input ("Invalid entry, please hit enter and try again...")