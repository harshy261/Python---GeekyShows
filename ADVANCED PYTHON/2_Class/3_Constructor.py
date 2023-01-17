# CONSTRUCTOR

# For initializing the instance variable of a class. 
# A class is constructor, if defined is called whenever a program create an object of that class.
# Constructor is called only once at the time of creating an instance.

# If two instances are created for a class, the constructor will be called once for each instance.




# # Constructor without Parameter >>>>>
# class Myclass:
#     def show(self):
#         print("I am a Method")

# x = Myclass()
# x.show()




# # Constructor with Parameter >>>>>
# class Mobile:
#     def __init__(self, m):
#         self.model = m

# realme = Mobile()




class Mobile:
    def __init__(self, m, v=30):
        self.model = m
        self.volumn = v

    def show_model(self, p):
        price = p
        print("Model: ", self.model, "and Price: ", price)
        print("Volumn: ", self.volumn)

# Passing Argument to Constructor
redmi = Mobile('Redmi 7s', 50)

# Accessing Method from Outside Class
redmi.show_model(1000)




