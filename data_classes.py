from dataclasses import dataclass, field


# @dataclass automatically generates __init__(), __repr__(), and __eq__() by default.
@dataclass(frozen=True)
class Employee:
    name: str
    age: int
    salary: float
    password: str = field(repr=False)
    mylist: list[int] = field(default_factory=list)
    department: str = "IT"

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary can not be negative")


emp1 = Employee("Ali", 30, 2500.5, "12345", "HR")
emp2 = Employee("Sara", 25, 5000, "123456")
emp2.mylist = [1, 2, 3]

print(emp1)
print(emp2.mylist)
print(emp1 == emp2)
