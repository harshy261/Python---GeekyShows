# GETTING INPUT FROM USERS

a = []
n = int(input("Enter Number of Elements:"))

for i in range(n):
    a.append(int(input("Enter Element : ")))

print(type(a))

a = tuple(a)

print(type(a))

print("Tuples: ")
for element in a:
    print(element)





