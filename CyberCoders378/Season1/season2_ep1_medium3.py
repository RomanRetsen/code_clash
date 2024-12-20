"""
We have a series of person and their birthdays in input.txt.
We need to search for the oldest and the youngest person.

The answer to give is difference between oldest and youngest counted in days"

"""
import datetime

the_list = []

with open("med3_input.txt", "r") as f:
    while not(read_line := f.readline().strip()) == "":
        year, month, day = [int(x) for x in read_line.split(",")[-1].split("-")]
        the_list.append((read_line.split(",")[-1], (year, month, day)))

oldest, *the_rest, yangest = sorted(the_list, key=lambda x:x[1])
oldest_date = datetime.date.fromisoformat(oldest[0])
yangest_date = datetime.date.fromisoformat(yangest[0])
print((yangest_date - oldest_date).days)
