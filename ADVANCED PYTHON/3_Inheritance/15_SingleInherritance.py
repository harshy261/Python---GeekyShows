# SINGLE INHERITANCE

class Father:
    money = 1000

    def show(self):
        print("Parent Class Instances Method")

    @classmethod
    def showmoney(cls):
        print("Parent Class Class Method: ", cls.money)

    @staticmethod
    def stat():
        a = 10
        print("Parent class static method =", a)


class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

f = Father()
s = Son()

s.disp()
s.show()
s.showmoney()
s.stat()
print()

f.show()
f.showmoney()




