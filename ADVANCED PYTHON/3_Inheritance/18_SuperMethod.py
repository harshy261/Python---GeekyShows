# CONSTRUCTOR WITH SUPER() METHOD

# If we write constructor in both the classes, parent class, child class, then the parent class constructor is not available to the child class.

# In this case only child class constructor is accessible which means child class constructor is replacing parent class constructor. 

# Super() Method is used to call parent class constructor or methods from the child class.



class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def __init__(self, m, j):
        super().__init__(m)
        self.job = j
        print("Son Class Contructor")

    def disp(self):
        print("Son Class Instance Method ", self.money, "Job: ", self.job)


s = Son(1000, 'Python')
s.disp()



