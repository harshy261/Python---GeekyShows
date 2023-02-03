# ABSTRACT CLASS ----> A class derived from ABC class which belongs to abc module, is known as abstract class in Python.

# Abstract class can have abstract method and concrete methods.

# Abstract class needs to be extended and its method implemented.

# PVM cannot create objects of an abstract class.

# Abstract Method ----> A abstract method is a method whose action is redefined in the child classes as per the requirement of the object.

# We can declare a method as abstract method by using @abstractmethod decorator.

# Concrete Method ----> A concrete Method is a method whose action in the abstract class itself.

# We use ABSTRACT CLASS when there are some common feature shared by all the objects as they are.


from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print('Concrete Method')

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Class")

c = Child()
c.disp()
c.show()





class DefenceForce (ABC):
    def __init__(self):
        self.id = 100

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47", self.id)

class Army(DefenceForce):
    def area(self):
        print("Army Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("Airforce Area = Sky")

class Navy(DefenceForce):
    def area(self):
        print("Navy Area = Sea")

a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print()

af.gun()
af.area()
print()

n.gun()
n.area()
print()


