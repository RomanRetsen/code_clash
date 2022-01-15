import csv
from random import randint

headers = ['randint upto 10', 'randint ipto 100', 'randint upto 1000']
rows = [{'randint upto 10' : randint(1,10), 'randint ipto 100':randint(1,100), 'randint upto 1000':randint(1,1000)}
        for _ in range(10)]
print(rows)

with open("random.csv", "wt") as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)