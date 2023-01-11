# GETTING SET INPUT FROM USER

a = set()

print(id(a))

n = int(input("Enter number of elements : "))

for i in range(n):
    el = input("Enter Element: ")
    a.add(el)

print(a)
print(id(a))








