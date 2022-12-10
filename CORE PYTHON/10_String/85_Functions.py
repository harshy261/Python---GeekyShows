# FUNCTIONS - Subprogram which are used to compute certain values or expressions

# Reusability, Code Maintenance, Debbugging, add or remove 

# def Function_name():
# def Function_name(para1, para2):

# function_name()


# def add():
#     a = 10
#     b = 20
#     c = a + b
#     print(c)
# add()



# def add(y):
#     x = 10
#     sum = x+y
#     print(sum)
# add(10)

# Parameter 'y' do not know which type of value they are about to receive till the value is passed at the time of calling the function. It means the type of data is determined only during runtime not at compile time. This is called Dynamic Typing.





# # Creating Function
# def disp():
#     print("Hello Harsh")

# # Calling a function
# disp()
# disp()
# disp()
# disp()




# def add():
#     a = 30
#     b = 20
#     print(a+b)

# add()


# def sub():
#     a = 30
#     b = 20
#     print(a-b)

# sub()




# return -- return something from the function. It is possible to return one or more values in python

def ADD():
    x = 10
    y = 5
    c = x+y
    return c

sum = ADD()
print(sum)




def ADD():
    x = 10
    y = 5
    return x+y

sum = ADD()
print(sum)




def ADD():
    x = 10
    y = 5
    c = x+y
    d = x-y
    return c,d

sum,sub = ADD()         # sum, sub = 15,5
print(sum)
print(sub)







