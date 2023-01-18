# STATIC METHOD

# Static method are used when some processing is related to the class but does not need the class or its instances to perform any work. 
# We use static method when we want to pass some values from outside and perform some action in the method.
# Decorator @staticmethod need to write above the static method. 


# Without Parameter

class Mobile:
    fp = 'Yes'

    @staticmethod 
    def show_model():
        print("FingerPrint: ", Mobile.fp)

realme = Mobile()
Mobile.show_model()









# With Parameter

class Mobile:
    fp = 'Yes'

    @staticmethod 
    def show_model(m, p):
        model = m
        price = p
        print("Model: ", model, "Price: ", price)

realme = Mobile()
Mobile.show_model('Realme X', 1000)

