# MULTI LEVEL INHERITANCE

# Father Class --> Son class --> GrandSon class 

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


class GrandSon(Son):
    def __init__(self):
        print("GrandSon Class Constructor")

    def showG(self):
        print("GrandSon Class")


g = GrandSon()
g.showF()
g.showS()
g.showG()



