# Types of Variable

# 1. Instance Variables  -->
#  Variables whose seperate copy is created in every object.
#  Instance Variable are defined and initialized using a constructor with self parameter




class Mobile:
    def __init__(self):
        self.model = 'Realme X'

    def show_model(self):
        print(self.model)

realme = Mobile()
redmi = Mobile()
geek = Mobile()

print(realme.model)
print(redmi.model)
print(geek.model)


redmi.model = 'Redmi 7s'
print(realme.model)
print(redmi.model)
print(geek.model)
print()









