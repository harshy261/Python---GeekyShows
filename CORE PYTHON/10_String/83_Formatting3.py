# F-String / Formatted String literal


# # Integer
# a = 10
# b = 20
# value = f" {a} "
# print(value)



# # Float
# c = 10.23
# d = 13.43
# print(f"{c}")
# print(f"{c} {d}")
# print(f"{d} {c}")



# # String 
# print("*********String*********")
# f_name = "Harsh"
# l_name = "Yadav"
# print(f"{f_name}")
# print(f"{f_name} {l_name}")
# print(f"{l_name} {f_name}")



# # Integer & String 
# print("*********String*********")
# name = "Harsh"
# age = 10
# print(f"Hello my name is {name}")
# print(f"{name} {age}")
# print(f"{age} {name}")



# price = 1234567890
# print(f"{price:,}")
# print(f"{price:_}")


# name = "Harsh"
# age = 19
# print(f"My name is {name} and age is {age} ")



# a = 50
# b = 3
# print(f"{a/b:.2}")



# name = "Harshyadav"
# print(f"{name.upper()}")

# name = "HARSHYADAV"
# print(f"{name.lower()}")



# print(f"{obj.name}")


# print(f"{{10}}")




# Date and Time

from datetime import datetime

today = datetime(2022,12,8)
print(f"{today}")
print(f"{today: %d-%b-%Y}")
print(f"{today: %d/%b/%Y}")
print(f"{today: %d,%b,%Y}")
print(f"{today: %d %b, %Y}")








