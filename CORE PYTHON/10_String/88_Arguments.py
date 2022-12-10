# ACTUAL ARGUMENTS -- function call arguments

# FORMAL ARGUMENTS -- function definition parameters 

# def add(a,b):               # (a,b) - formal arguments
#     c = a+b
#     print(c)

# add(10,20)                  # (10,20) - actal arguments




# # TYPE OF ACTUAL ARGUMENT :-

# # positional argument
# def pw(x,y):
#     z = x**y
#     print(z)
# pw(5,2)
# pw(2,5)
# pw(3,2,5)


# # keyword argument
# def show(name, age):
#     print(name, age)
#     print(f"Name: {name} Age: {age}")

# show(name= "HarshYadav", age = 43)
# show(age = 43, name= "HarshYadav")

# show(43, "HarshYadav")
# show("HarshYadav", 43)


# # default arguments
# def show(name, age = 27):
#     print(name, age)

# show(name="HarshYadav")
# show(name="HarshYadav", age = 43)


# variable length arguments
# store values in tuple
# def add(*num):
#     z = num[0]+num[1]+num[2]
#     print(z)
# add(5,4,3)

# def add(x,*num):
#     z = x+num[0]+num[1]+num[2]
#     print(z)
# add(5,4,3,6)


# keyword variable length arguments
def add(**num):
    z = num['a']+num['b']+num['c']
    print(z)
add(a=5, b=11, c=45)

def add(x, **num):
    z = x+num['b']+num['c']
    print(z)
add(5, b=11, c=45)




