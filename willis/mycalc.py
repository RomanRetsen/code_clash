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
        return round(number1 / number2, 2)
    else:
        return None

def do_oper_by_id(operation_id):
    number1 = int(input("Enter 1-st number"))
    number2 = int(input("Enter 2-d number"))
    if operation == "1":
        return number1 + number2
    elif operation == "2":
        return number1 - number2
    elif operation == "3":
        return number1 * number2
    elif operation == "4":
        return round(number1 / number2, 2)
    else:
        return None


while True:
    top_menu = input("Type number (1,2) of operation or 'exit' to quit program\n"
                     " 1) Math operation\n"
                     " 2) exit\n>>> ")
    if top_menu == "1":
        while True:
            operation = input("Type name of math operation you'd like to perform. \n"
                              "You option: add(1), subtract(2), multiply(3), divide(4) \n"
                              "OR enter 'back' to go back to main menu >>> ")
            if operation in ["add", "subtract", "multiply", "divide"]:
                result = do_oper(operation)
                if result:
                    print("-------------------------------------")
                    print("Result of the operation: " + str(result))
                    print("-------------------------------------")
                else:
                    print("-------------------------------------")
                    print("Operation error")
                    print("-------------------------------------")
            elif operation in ["1", "2", "3", "4"]:
                result = do_oper_by_id(operation)
                if result:
                    print("-------------------------------------")
                    print("Result of the operation: " + str(result))
                    print("-------------------------------------")
                else:
                    print("-------------------------------------")
                    print("Operation error")
                    print("-------------------------------------")
            elif operation.lower() == 'back':
                break
            else:
                print("-------------------------------------")
                print("Wrong operation.      Try again     ")
                print("-------------------------------------")
                continue
    elif top_menu == "2" or top_menu == "exit":
        print("Bye-bye")
        break
    else:
        print("Wrong option. Try again")
        continue

