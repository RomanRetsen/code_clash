from datetime import datetime
from datetime import date

class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    def get_age(self):
        return (date.today()- self.birthdate.date()).days

    def __sub__(self, other):
        return (self.birthdate - other.birthdate).days

    def __repr__(self):
        return f"{self.first_name} {self.last_name} who was born {self.birthdate}"

def read_file(filename):
    the_persons_list = []
    with open(filename) as file:
        for line in file:
            fname, lname, birth = line.strip().split(",")
            the_persons_list.append(Person(fname, lname, birth))
    return the_persons_list


def find_oldest_person(people):
    return min(people,  key=lambda x:x.birthdate)


def find_youngest_person(people):
    return max(people,  key=lambda x:x.birthdate)


def main():
    persons = read_file(r"C:\Container\Downloads\4.txt")
    oldest_person = find_oldest_person(persons)
    print(oldest_person)
    youngest_person = find_youngest_person(persons)
    print(youngest_person.get_age())
    print(youngest_person - oldest_person)


if __name__ == '__main__':
    main()