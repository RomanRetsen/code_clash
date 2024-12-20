#########1
employee_name = "Rom"
ID = 1
is_employed = True
##########2
modified_name = employee_name[3:] if len(employee_name) >=3 else "Error. Name has less than 3 chars"
print(modified_name)
##########3
animals = ["Tiger", "Lion", "Bison", "Rabbit", "Snake"]
vehicles = ["Toyota", "Honda", "Tesla", "Chevrolet", "Audi"]
animals.append("Crocodile")
animals.append("Fox")
vehicles.append("Ford")
vehicles.append("Dogdge")
print(*animals)
print(*vehicles)
##########4
print("Half of the name is ->>  " + employee_name[:(len(employee_name)//2)]) if len(employee_name) > 1 \
    else print("Error. Name is too short to be divided")