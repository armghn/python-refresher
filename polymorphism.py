# Polymorphism:
#   1.Runtime Polymorphism (Method overriding) -> Same method, Different behavior based on the object type.
#   2.Compile-time polymorphism (Method overloading) -> Same name, Different behavior based on inputs. (Python doesn't support it by method signatures alone.)
#   3.Duck typing → Python uses an object's available behavior rather than requiring a specific type.


#Runtime
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()



#Compile-tiem
def add(*args):
    return sum(args)


print(add(2, 3))        # 5
print(add(2, 3, 4))     # 9


#duck typing -> Both objects work even though they don't share a parent class.
class Duck:
    def speak(self):
        print("Quack")


class Person:
    def speak(self):
        print("Hello")


def make_it_speak(obj):
    obj.speak()


make_it_speak(Duck())
make_it_speak(Person())
