# Instance Method

# Acts upon the instance variable of the class.



# Instance Method w/o Parameters

class Mobile:
    def __init__(self):
        self.model = 'Realme X'

    def show_model(self):
        print("Model: ", self.model)

realme = Mobile()
realme.show_model()

print()




# Instance Method with Parameters

class Mobile:
    def __init__(self):
        self.model = 'Realme X'

    def show_model(self, p):
        self.price = p
        print("Model: ", self.model, "Price: ", self.price)

realme = Mobile()
realme.show_model(1000)




