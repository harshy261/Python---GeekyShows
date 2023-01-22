# CONSTRUCTOR IN INHERITANCE

# By Default , the contructor in the parent class is available to the child class.

class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def disp(self):
        print("Son Class Instance Method ")


s = Son()
print(s.money)
s.show()
s.disp()










class Father:
    def __init__(self, m):
        self.money = m
        print("Father Class Constructor")
    
    def show(self):
        print("Father Class Instance Method")


class Son(Father):
    def disp(self):
        print("Son Class Instance Method ", self.money+1000)


s = Son(5000)
print(s.money)
s.show()
s.disp()







