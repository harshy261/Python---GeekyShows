# HIERARCHICAL INHERITANCE

# SINGLE PARENT CLASS --> MULTIPLE CHILD CLASS


class Father:
    def __init__(self):
        print("Father Class Constructor")

    def showF(self):
        print("Parent Class")

class Son(Father):
    def __init__(self):
        print("Son Class Constructor")

    def showS(self):
        print("Son Class")


class Daughter(Father):
    def __init__(self):
        print("Daughter Class Constructor")

    def showD(self):
        print("Daughter Class")


s = Son()
s.showS()
s.showF()

# s.showD()            # Shows Error 

d = Daughter()
d.showD()
d.showF()







