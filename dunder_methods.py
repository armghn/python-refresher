class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"

    def __add__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        sums = self.age + other.age
        return sums

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age


class Employee:
    def __init__(self, employees):
        self.employees = employees

    def __len__(self):
        return len(self.employees)

    def __contains__(self, item):
        return item in self.employees

    def __repr__(self):
        return repr(self.employees)


p1 = Person("Ali", 25)
p2 = Person("Sara", 20)
p3 = Person("hasan", 25)

emps = Employee([p1.name, p2.name, p3.name])

print(p1)
print(repr(p1))
print(p2)
print(repr(p2))
print(p1 + p2)
print(p1 == p2)
print(p1 == p3)
print(len(emps))
print(emps)
print("Sara" in emps)
