from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Commission:
    commission: float = 100
    contracts_landed: int = 0

    def get_payments(self) -> float:
        return self.commission * self.contracts_landed

@dataclass
class Employee(ABC):
    name: str
    id: int

    @abstractmethod
    def compute_pay(self)->float:
        '''Some string describing abstract method'''

@dataclass
class HourlyEmployee(Employee):
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self):
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
        )

@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    commission: float = 100
    contracts_landed: int = 0

    def compute_pay(self):
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class SalariedEmployee(Employee):
    commission: float = 100
    contracted_landed: int = 0
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self):
        return (
            self.monthly_salary * self.percentage
            + self.commission * self.contracted_landed
        )

@dataclass
class Freelancer(Employee):
    commission: float = 100
    contracted_landed: int = 0
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self):
        return (self.commission * self.contracted_landed + self.pay_rate * self.hours_worked)

def main():
    henry = HourlyEmployee(name="Henry", id=12345, pay_rate=50, hours_worked=100)
    print(hash(henry))
    # henry2 = HourlyEmployeeWithCommission(name="Henry2", id=92345, pay_rate=50, \
    #                                       hours_worked=100, contracts_landed=2)
    # print(henry.compute_pay())
    # print(henry2.compute_pay())
    # sarah = SalariedEmployee(name="Sarah", id=54321, monthly_salary=5000, contracted_landed=10)
    # print(sarah.compute_pay())


if __name__ == "__main__":
    main()

