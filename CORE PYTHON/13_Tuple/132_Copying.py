# Copying Tuple


a = (1, 2, 3, 4, 5)
b = a

print("A : ", a)
print("B : ", b)

print("ID of A ", id(a))
print("ID of B ", id(b))

print()
b = a[0:5]

print("A : ", a)
print("B : ", b)

print("ID of A ", id(a))
print("ID of B ", id(b))
