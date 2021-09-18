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

student_database = ["student1", "student2", "student3", "student4", "student5", "student6", "student7", "student8"]
entering_student = input("Enter your name: ")

if entering_student in student_database:
    print("Welcome, " + entering_student)
    print("You are a part of something bigger")
    while True:
        operation = input("Type name of math operation you'd like to perform. \n"
                          "You option: add, subtract, multiply, divide \n"
                          "OR enter exit to quit the program >>> ")
        if operation in ["add", "subtract", "multiply", "divide"]:
            result = do_oper(operation)
            if result:
                print("Result of the operation: " + str(result))
            else:
                print("Operation error")
        elif operation.lower() == 'exit':
            print("Bye-bye")
            break
        else:
            print("Wrong operation. Try again")
            continue

else:
    print("Hello, " + entering_student)
    print("You are a stranger to us. Bye-bye")