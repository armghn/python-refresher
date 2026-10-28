class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12

    def increase(self):
        self.pay *= 1.1


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.emp_salary = Salary(self.pay)

    def annual_salary(self):
        return f"Total: {self.emp_salary.get_total() + self.bonus}"


emp1 = Employee(1000, 10)
print(emp1.annual_salary())
# Composition represents a “has-a” relationship between objects.