# CLASS ---------->  

# Python Class is group of Attributes and methods

# Attributes are represented by variable that contains data.
# Method performs an action or task. It is similar to function.

# Object represent the base class name from where all classes in Python are derived. This class is also derived drom Object class. This is optional. 

# __init__() ---> This method is used to initailizes the variables. This is a special Method. W edo not call this method explicitly.

# self is a default variable that contains the memory address of the current object.



# OBJECTS --------->

# Object is class type variable or class instances. To use a class, we should create an object to the class.


# # 1 >>>>
# class Myclass(object):
#     def show(self):
#         print("I am a Method")

# x = Myclass()
# x.show()




# # 2 >>>>
# class Mobile:
#     def __init__(self):
#         self.model = 'RealMe X'

#     def show_model(self):
#         print("Model: ", self.model)

# realme = Mobile()
# realme.show_model()

# print(realme.model)






# # 3 >>>>
# class Mobile:
#     def __init__(self, m):
#         self.model = m

#     def show_model(self, p):
#         price = p
#         print("Model: ", self.model, "Price: ", price)

# realme = Mobile()
# realme.show_model(1000)







# 4 >>>>
class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        self.price = p
        print("Model: ", self.model, "Price: ", self.price)

realme = Mobile('Realme X')
realme.show_model(1000)
print(id(realme))
print()

redmi = Mobile('Redmi 7s')
redmi.show_model(2000)
print(id(redmi))
print()

geek = Mobile('Python')
geek.show_model(49)
print(id(geek))















