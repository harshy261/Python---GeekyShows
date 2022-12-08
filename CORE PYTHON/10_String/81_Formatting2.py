# STRING FORMATTING USING format() method

# str,format(arg)

# str = "My age is {}"
# print(str.format(62))

# print("My age is {}".format(62))


# # Int or Float or String
# print("{}".format(10))
# print("{} {}".format(10,20))
# print("{0}".format(10))
# print("{0} {1}".format(10,20))
# print("{1} {0}".format(10,20))
# print("{num1}".format(num1=10))
# print("{num1} {num2}".format(num1=10,num2=20))
# print("{num2} {num1}".format(num1=10,num2=20))


# print("{} {}".format(10.23,20.45))

# print("{} {}".format("Yadav","Harsh"))



# print("{num:5d}".format(num=15))
# print("{num:05d}".format(num=15))
# print("{num:+5d}".format(num=15))
# print("{num:<5d}".format(num=15))
# print("{num:*<5d}".format(num=15))
# print("{num:*>5d}".format(num=15))
# print("{num:^5d}".format(num=15))
# print("{num:*^5d}".format(num=15))


# print("{num:f}".format(num=15.65))
# print("{num:f}".format(num=15.65))
# print("{num:8f}".format(num=15.65))
# print("{num:8.3f}".format(num=15.65))
# print("{num:+8.2f}".format(num=15.65))
# print("{num:<8.2f}".format(num=15.65))
# print("{num:*<8.2f}".format(num=15.65))
# print("{num:*>8.2f}".format(num=15.65))
# print("{num:^8.2f}".format(num=15.65))
# print("{num:*^8.2f}".format(num=15.65))


# print("{:s}".format("HarshYadav"))
# print("{:s}".format("HarshYadav"))
# print("{:8s}".format("HarshYadav"))
# print("{:8.3s}".format("HarshYadav"))
# print("{:8.2s}".format("HarshYadav"))
# print("{:<8.2s}".format("HarshYadav"))
# print("{:*<8.2s}".format("HarshYadav"))
# print("{:*>8.2s}".format("HarshYadav"))
# print("{:^8.2s}".format("HarshYadav"))
# print("{:*^8.2s}".format("HarshYadav"))




print("{:,}".format(1234567890))
print("{:_}".format(1234567890))


name = "Harsh"
age = 62
print("My name is {} and age is {} ".format(name,age))



a = 50
b = 3
print("{:.2%}".format(a/b))


value = (10,20)
print("{0[0]} {0[1]}".format(value))


data1 = {'rahul': 2000, 'sonam':3000}
print("{0[rahul]:d} {0[sonam]:d}".format(data1))
print("{x[rahul]:d} {x[sonam]:d}".format(x=data1))
print("{rahul} {sonam}".format(**data1))







