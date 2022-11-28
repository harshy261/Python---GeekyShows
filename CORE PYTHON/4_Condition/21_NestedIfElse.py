# Nested If Else


# 1 -----
a = int(input("Enter your Number a: "))
if(a>10):
    print("a is greater than 10")
    if(a<20):
        print("a is between 10 to 20 ")
else:
    print("a is less than 10 ")
print("Code Ended")



# 2 -----
x = 10
y = 20
z = 30
k = int(input("Enter your Number k: "))
if(k>x):
    print("k is greater than 10")
    if(k>y):
        print("k is greater than 20")
        if(k>z):
            print("k is greater than 30")
        else:
            print("k is between 20 to 30 ")
    else:
        print("k is between 10 to 20")
else:
    print("k is less than 10")



