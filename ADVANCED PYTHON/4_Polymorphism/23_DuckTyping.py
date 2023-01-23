# DUCK TYPING

# The type of object is distinguished only at runtime.

class Duck:
    def walk(self):
        print("thapak thapak thapak")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow Meow")

def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

# c = Cat()             
# myfunction(c)             # Shows error




