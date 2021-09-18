import os

def clear():
    # print(os.name)
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def add_student():
    clear()
    student_name = input("Enter student's name->>")
    student_course = input("Enter student's enrolled course (ASA, BSA and CSA)->>")
    student_tuition = int(input("Enter student's initial tuition fees deposit amount->>"))
    student_marks = [int(x) for x in input("Enter student's marks space separated->>").split()]
    return (student_name, student_course, student_tuition, student_marks)

def print_student_marks(students):
    clear()
    print("LIST OF STUDENTS AND THIER MARKS")
    for student in students:
        print(f"{student[0]}  has such marks: ", *student[3])

def print_student_tuition(students):
    clear()
    print("LIST OF STUDENTS AND THIER TUITION AMOUNT PAID")
    for student in students:
        print(f"{student[0]}  has tuition paid in an amount: ", student[2])

def print_student_ip(students):
    clear()
    print("LIST OF STUDENTS AND THEIR CORESPONDING IP")
    for ip_index, student in enumerate(students, 1):
        if ip_index < 255:
            print(f"Student {student[0]} has ip 192.168.14.{ip_index}")
        else:
            print(f"College does not have assign ip address for student {student[0]}")

#database of students with initial 2 studetns keyed in
students = [('Nigel', 'CSA', 3000, [75, 80, 95]), ('Benson', 'CSA', 4000, [76, 81, 96])]
while True:
    top_menu = input("Type number (1,2,3,4,5,6,7) of operation or 'quit' to exit the program\n"
                     " 1) Add Student\n"
                     " 2) Print Students and Marks\n"
                     " 3) Find out highest mark\n"
                     " 4) Check existance of the student in the database\n"
                     " 5) Print students and paid tuition\n"
                     " 6) Print IP ranges of the student\n"
                     " 7) quit\n>>> ")
    if top_menu == "1":
        entered_student = add_student()
        if not entered_student[0] in [x[0] for x in students]:
            students.append(entered_student)
            print(f"Student {entered_student[0]} was added to the database ")
        else:
            print("Entered Student exists\nEntered data is ignored.")
    elif top_menu == "2":
        print_student_marks(students)
        input("Press Any Key To Continue")
    elif top_menu == "3":
        clear()
        print("Highes mark: ", end="->>")
        print(max([max(x[3]) for x in students]))
        input("Press Any Key To Continue")
    elif top_menu == "4":
        clear()
        print("Checking if student exists in the database")
        check_student = input("Enter student->>")
        if check_student.lower() in [x[0].lower() for x in students]:
            print(f'Student {check_student} DOES exists in the database')
        else:
            print(f'Student {check_student} does NOT exists in the database')
        input("Press Any Key To Continue")
    elif top_menu == "5":
        print_student_tuition(students)
        input("Press Any Key To Continue")
    elif top_menu == "6":
        print_student_ip(students)
        input("Press Any Key To Continue")
    elif top_menu == "7" or top_menu == "quit":
        print("Bye-bye")
        break
    else:
        print("Wrong option. Try again")
        continue

