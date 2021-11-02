# class Marks:
#     def __init__(self, marks):
#         self.marks = marks
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def calculate_avg(self):
#         return sum(self.marks) / len(self.marks)
#
# marks_obj = Marks([12,34, 56, 78, 54])
#
# print(marks_obj.calculate_avg())
# marks_obj.add_mark(100)
# print(marks_obj.calculate_avg())

# class Car:
#     def __init__(self, name, year, kilom):
#         self.brand = name
#         self.year = year
#         self.mileage = kilom
# 
#     def kilo(self):
#         print(f"The mileage of the car is {self.mileage}")
# 
# 
# car1 = Car("Toyota Rav4", 2021, 5000)
# car2 = Car("Lexus RX350", 2022, 10000)
# # toyota = Car("Toyota", 2000, 100000)
# # suzuki = Car("Suzuki", 1999, 150000)
# 
# list_of_cars = [car1, car2]
# 
# for car in list_of_cars:
#     print(car.brand)

# class IceCream:
#     def __init__(self, type):
#         self.ice_type = type
#
#     def __str__(self):
#         return (f"This is ***{self.ice_type}*** type of icecream")
#
#
# def create_three_icecreams():
#     cone_icecream = IceCream("ice")
#     cup_icecream = IceCream("cup")
#     bar_icecream = IceCream("bar")
#     return [cone_icecream, cup_icecream, bar_icecream]
#
# for ice_cream in create_three_icecreams():
#     print(ice_cream)

class SoftDrink:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

list_of_list = [
    SoftDrink("pepci", 6),
    SoftDrink("coke", 3),
    SoftDrink("nestea", 18)
]

while True:
    user_choice = input("Enter drink of your choice (pepci, coke, nestea). with norm temp(6,3,18) \n"
                        "OR type 'exit' to exit:> ")
    if user_choice in [x.name for x in list_of_list]:
        choice = [x for x in list_of_list if x.name == user_choice][0]
        temperature = input("input drinks temperature:> ")
        if int(choice.temperature) < int(temperature):
            print("  Drink is expired!!! :> ")
    elif user_choice == "exit":
        break
    else:
        continue