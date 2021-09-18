def do_oper(operation):
    number1 = int(input("Enter 1-st number"))
    number2 = int(input("Enter 2-d number"))
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        return number1 / number2
    else:
        return None

def do_hst():
    value = int(input("Enter value to calculate HST on (integer value only)"))
    return value * 0.13


while True:
    top_menu = input("Type number (1,2) of operation or 'exit' to quit program\n"
                     " 1) Calculate HST \n"
                     " 2) Math operation\n"
                     " 3) exit\n>>> ")
    if top_menu == "1":
        result = do_hst()
        if result:
            print("Result of the operation: " + str(result))
        else:
            print("Operation error")
    elif top_menu == "2":
        while True:
            operation = input("Type name of math operation you'd like to perform. \n"
                              "You option: add, subtract, multiply, divide \n"
                              "OR enter 'back' to go back to main menu >>> ")
            if operation in ["add", "subtract", "multiply", "divide"]:
                result = do_oper(operation)
                if result:
                    print("Result of the operation: " + str(result))
                else:
                    print("Operation error")
            elif operation.lower() == 'back':
                break
            else:
                print("Wrong operation. Try again")
                continue
    elif top_menu == "3":
        print("Bye-bye")
        break
    else:
        print("Wrong option. Try again")
        continue

