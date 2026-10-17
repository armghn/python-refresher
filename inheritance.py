class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        inf = f"Name is {self.name}"
        return inf

    def sound(self):
        return "Animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        det = f"Name is {self.name}, Breed is {self.breed}"
        return det

    #runtime polymorphism using method overriding
    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    #runtime polymorphism using method overriding
    def sound(self):
        return "Meow"


a = Animal("AmirMorabba")
d = Dog("lara", "Golden Retriever")
c = Cat("Mute", "Ginger")

animals = [a, d, c]
print(f"Info: {d.info()}")
print(f"Details: {d.details()}")

for animal in animals:
    print(animal.sound())

