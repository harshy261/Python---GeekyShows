# CLASS METHOD

# class method are the methods which act upon the class variables or static variable of class.

# Decorator @classmethod need to write above class method.
# By Default, the first parameter of class method is 'cls' which refers to class itself.


class Mobile:
    @classmethod                    # Decorator
    def show_model(cls):            # Class Method
        print("Realme X")

realme = Mobile()
Mobile.show_model()                 # Calling Class Method





# Without Parameter

class Mobile:
    fp = 'Yes'

    @classmethod                    # Decorator
    def show_model(cls):            # Class Method
        print("Fingerprint: ", cls.fp)

realme = Mobile()
Mobile.show_model()                 # Calling Class Method





# With Parameter


class Mobile:
    fp = 'Yes'

    @classmethod                        # Decorator
    def show_model(cls, r):             # Class Method
        cls.ram = r
        print("Fingerprint: ", cls.fp)
        print("RAM: ", cls.ram)

realme = Mobile()
Mobile.show_model('4GB')                 # Calling Class Method




