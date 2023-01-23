# METHOD OVERRIDING

# If we write method in both classes, parent class and child class then the parent class's method is not available to child class.

# In this case only child class's method is accessible which means child class's method is replacing.

# Method overriding is used when programmer want to modify the existing behaviour of method



# 1 >>>>
class Add:
    def result(self, a , b):
        print("Addition: ", a+b)

class Multi(Add):
    def result(self, a, b):
        print("Multiplication: ", a*b)

m = Multi()
m.result(10, 20)




# 2 >>>>
class Add:
    def result(self, a , b):
        print("Addition: ", a+b)

class Multi(Add):
    pass

m = Multi()
m.result(10, 20)




# 3 >>>>
class Add:
    def result(self, a , b):
        print("Addition: ", a+b)

class Multi(Add):
    def result(self, a, b):
        super().result(30, 50)
        print("Multiplication: ", a*b)

m = Multi()
m.result(10, 20)




