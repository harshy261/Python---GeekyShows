# CONSTRUCTOR OVERRIDING

# If we wright constructor in both classes, parent class and child class the the parent class constructor is not available to the child class. 

# In this case only child class constructor is accessible which means child class constructor is replacing parent class constructor. 

# Constructor Overriding is when programmer want to modify the existing behaviour of a constructor.




class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def __init__(self):
        self.money = 5000
        self.car = 'BMW'
        print("Son Class Contructor")

    def disp(self):
        print("Son Class Instance Method ")


s = Son()
print()

print(s.money)
print(s.car)

s.disp()
s.show()








class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def __init__(self, r):
        self.money = r
        self.car = 'BMW'
        print("Son Class Contructor")

    def disp(self):
        print("Son Class Instance Method ")


s = Son(2000)
print()

print(s.money)
print(s.car)

s.disp()
s.show()









