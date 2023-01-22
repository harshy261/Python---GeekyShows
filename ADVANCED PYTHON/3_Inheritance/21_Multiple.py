# MULTIPLE INHERITANCE

# Multiple Parent Class --> Single Child Class



class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")

    def showF(self):
        print("Parent Class")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Constructor")

    def showM(self):
        print("Mother Class")


class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")

    def showS(self):
        print("Son Class")


s = Son()
s.showF()
s.showM()
s.showS()

# In Case of using SUPER() method >>> Father Constructor is called
# Use SUPER() method in every and all constructor to call every constructor

