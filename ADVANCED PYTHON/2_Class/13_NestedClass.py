# NESTED CLASS

class Army:
    def __init__(self):
        self.name = 'Rahul'
        self.gn = self.Gun()

    def show(self):
        print("Name: ", self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Rounds'
            self.length = '34.3 inch'

    def disp(self):
        print("Gun Name: ", self.name)
        print("Capacity: ", self.capacity)
        print("Length: ", self.length)


a = Army()
print(a)
print(a.name)
a.show()

g = Army().Gun()
print()

print(g.name)
print(g.capacity)
print(g.length)
print()

g.disp()

print(a.gn)
print(a.gn.name)

