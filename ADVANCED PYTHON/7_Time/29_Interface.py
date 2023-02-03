# INTERFACE 

# Interface is not explicitly available in Python

# Interface is an Abstract class which contain only abstract method but not a single concrete method.

# We use Interface when all the feature need to be implemented differently for different objects.


from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method")

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c = Child()
c.disp()



