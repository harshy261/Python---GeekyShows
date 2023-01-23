# STRONG TYPING

# hasattr() function is used to check whether the object has method or not.


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
    if hasattr(obj, 'walk'):
        obj.walk()

d = Duck()
myfunction(d)
print()

h = Horse()
myfunction(h)
print()

c = Cat()             
myfunction(c)  
