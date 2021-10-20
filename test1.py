# user_age = int(input("Enter your age: "))
# if user_age < 18:
#     print("You are minor. Please leave....")
# else:
#     print("Welcome!!")

# taks 2 . option1
# entered = input()
# if entered == "":
#     print("You did not entered anything. Try again")
# else:
#     print("Data eccepted")

# taks 2 . option2
# print("Empty") if input()=="" else print("something")

# count = 1
# while count == 1:
#     print("Infinite loop")
#     user_choice = input("Enter magic number to quit")
#     if user_choice == "18":
#         count = 2

# def myfunction123():
#     username = input("Enter your name>> ")
#     print(f"Hello {username}")
#
# myfunction123()
#

# def greet(x,y):
#     print("Welcome Mr.", x, "Your age is:", y)
#
# greet("Roman", 38)

# def add_func(x, y):
#     return x + y
#
# def sub_func(x, y):
#     return x - y
#
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# print("The result of addition is: ", add_func(a, b))
# print("The result of substruction is: ", sub_func(a, b))

# def the_func(a, b):
#     print(a + b)
#
# the_var = the_func(5 ,6)
# print(the_var)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupWindowItems()

    def setupWindowItems(self):
        self.setGeometry(0, 0, 500, 500)
        self.pushButton = QPushButton("Guess Number")
        self.pushButton.move(100, 100)

if __name__ == "__main__":
    myapp = QApplication([])
    my_window = SimpleWindow()
    my_window.show()
    myapp.exec()







