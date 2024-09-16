"""
We need to proces the list of all the products provided in the input.txt and find the sum of of all our assest.
But beware, there might has been some error in data entry for the input file that have to be handled without crashing the system!

"""
from decimal import Decimal


counter = 0
total_decimal = Decimal("0")
total = 0
with open("med1_input.txt", "r") as f:
    while not (read_line := f.readline().strip()) == "":
        the_value = "".join([x for x in read_line if x.isdigit() or x == "."])
        if len(the_value) > 0 and the_value.count(".") < 2:
            counter += 1
            total_decimal += Decimal(the_value)
            total += float(the_value)
print(f"Total in float {round(total, 2)}")
# print(f"Total in Decimal {total_decimal}")