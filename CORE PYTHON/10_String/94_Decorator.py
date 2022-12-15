# FUNCTION DECORATOR 

# A Decorator Function is a function that accepts a function as parameter and return a function
# A Decorator takes the result of a function, modifies the result and returns it.

# @function_name 



# def decor(fun):
#     def inner():
#         print(" IF: Before enhanncing Function")
#         fun()
#         print(" IF: After enhanncing Function")
#     return inner


# def num():
#     print("We will use this Function")
#     print("And we will enhance this in decorator")

# num()


# result_fun = decor(num)
# result_fun()














def decor(fun):
    def inner():
        print(" IF: Before enhanncing Function")
        fun()
        print(" IF: After enhanncing Function")
    return inner


def num():
    return 10

result_fun = decor(num)
print(result_fun())









