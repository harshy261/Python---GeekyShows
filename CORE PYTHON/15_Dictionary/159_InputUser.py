# TAKE INPUT FROM USER 

a = {}
n = int(input("Number of Elements: "))

for i in range(n):
        k = input("Enter keys: ")
        v = input("Enter value: ")
        a.update({k:v})

print(a)








