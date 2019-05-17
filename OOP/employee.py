import datetime


class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        print("Employee " + first + " " + last +
              " with email: " + self.email + " crated")
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str_1.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True


Henrique = Employee("Henrique", "Castro", 150000)
Fran = Employee("Franciele", "Bach", 500000)
Mari = Employee("Mariane", "Bach", 250000)
Maicon = Employee("Maicon", "Silva", 240000)
Tati = Employee("Tatiane", "Reis", 300000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

print(Henrique.fullname())
print(Employee.fullname(Henrique))

print(Henrique.pay)

# Henrique.raise_amount = 1.05

Employee.set_raise_amount(1.05)

Henrique.apply_raise()
print(Henrique.pay)

print(Henrique.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_employees)

new_empl_1 = Employee.from_string(emp_str_1)

print(new_empl_1.first)
print(new_empl_1.last)
print(new_empl_1.pay)
print(new_empl_1.email)


my_date = datetime.date(2016, 7, 10)
print(my_date)
print(Employee.is_workday(my_date))
