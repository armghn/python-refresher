class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            raise ValueError("Salary must be positive")


class SubEmployee(Employee):
    def show_age(self): # Demonstrates accessing a protected attribute from a subclass.
        return self._age


emp1 = Employee("Ali", 25, 5_000)
print(emp1._age)
print(emp1.salary)
emp1.salary = 7000
print(emp1.salary)
# print(emp1.__salary)     Error: Not accessible directly

subEmp1 = SubEmployee("hasan", "30", 8000)
print(subEmp1._age)
print(subEmp1.show_age())
