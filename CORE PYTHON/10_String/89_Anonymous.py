# Anonymous / Lambdas Functions

# not defined using 'def' but 'lambda'
# no return statements
# contain only expression
# can't include statements in body

# lambda argument_list:expression
# lambda x, y:x+y

# sum = lambda x:x+1
# print(5)

# add = lambda x,y:x+y
# print(add(5,2))

# add_sub = lambda x,y:(x+y,x-y)
# a, s = add(5,2)
# print(a)
# print(s)

# add = lambda x,y=3:x+y
# print(add(5,2))
# print(add(5))



# NESTED LAMBDA FUNCTION

# add = lambda x=10 : (lambda y:x+y)

# a = add()
# print(a(20))



# Passing lambda Function to another Function
# def show(a):
#     print(a(8))
# show(lambda x:x)

# Returning lambda function
def add():
    y = 20
    return (lambda x:x+y)
a = add()
print(a(10))



