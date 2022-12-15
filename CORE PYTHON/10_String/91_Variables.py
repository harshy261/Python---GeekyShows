# GLOBAL AND LOCAL VARIABLES

# a = 50              # Global Variable
# def show():
#     x = 10          # Local Variable
#     print(a)
#     print(x)

# show()
# # print("x:",x)
# print("a:",a)




# If we mention global variable and want to use it inside inspite of local variable .....

i = 10
def show():
    global i 
    i = 20
    print("A : ", i )

show()
print("A : ", i)



# GLOBAL FUNCTION
# RETURNS IN DICTIONARY

x = 10

def show():
    x = 10
    print("Local Variable X: ", x)
    k = globals()['x']
    print("K:",k)
    k = 40
    print("k:",k)


show()
print("Global Variable: X", x)












