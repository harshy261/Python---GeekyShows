# CLASS VARIABLE / STATIC VARIABLE

# Class Variable are the variable whose single copy is available to all the instances of the class.
# If we modify the copy of class variable in an instances, it will effect all the copies in the other instances.


class Mobile:
    fp = 'Yes'              # Class Variable

    @classmethod
    def is_fp(cls):
        print(cls.fp)       # Accessing Class Variable

realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("Realme: ", Mobile.fp)
print("Redmi: ", Mobile.fp)
print("Geek: ", Mobile.fp)










class Mobile:
    fp = 'Yes'                                # Class Variable

    def __init__(self):
        self.model = 'Realme X'

    def show_model(self):
        print("Model: ", self.model)

    @classmethod
    def is_fp(cls):
        print("Finger Print: ", cls.fp)       # Accessing Class Variable

realme = Mobile()
realme.show_model()
Mobile.is_fp()
print()
Mobile.fp = 'No'
Mobile.is_fp()









