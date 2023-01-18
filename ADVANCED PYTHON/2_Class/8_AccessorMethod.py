# ACCESSOR METHOD 

# used to access and read data of the variables. This method do not modify the data in the variable. This is also called as getter method.


class Mobile:
    def __init__(self):
        self.model = 'Realme X'

    def show_model(self):
        return self.model 

realme = Mobile()
realme.show_model()

print()