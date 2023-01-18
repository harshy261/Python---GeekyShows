# MUTATOR METHOD

# Used to access or read or modify data of the variables. This method modify the data in the variable. This is also called the setter method.

class Mobile:
    def __init__(self):
        self.model = 'Realme X'

    def show_model(self):
        self.model = 'Realme 2'

realme = Mobile()
# Before Setting
print(realme.model)
# After Setting
realme.set_model()
print(realme.model)

print()









class Mobile:
    def __init__(self, m):
        self.model = m

realme = Mobile()
realme.set_model('Realme X')
print(realme.model)
print()



