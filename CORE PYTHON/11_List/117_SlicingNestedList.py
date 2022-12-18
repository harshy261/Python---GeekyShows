# SLICING NESTED LIST

x = [ [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [11, 22, 33],
    [44, 55, 66],
    [12, 34, 56] ]

print("Original List")
print(x)
print()

print("From 1st Position to 4rth Position")
a = x[1:5]
print(a)
print()

print("From 0th Position to last Position")
a = x[0:]
print(a)
print()

print("From 0th Position to 4rth Position")
a = x[:5]
print(a)
print()

print("Last 4 List")
a = x[-4:]
print(a)
print()

print("From 0th Position to 6th Position stepsize 2")
a = x[:7:2]
print(a)
print()

print("Last 5 List with [-5-(-3)] = 2 List towards Right")
a = x[-5:-3]
print(a)
print()

print("Slice Nested 2nd Position, 0th Position")
a = x[2:3]
print(a)
g = x[2:3][0]
print(g)
print()

print("Slice 2nd List then extract elements")
h = x[2:3][0][0]
print(h)

i = x[2:3][0]
for el in i:
    print(el)
print()

print("Last Nested 4 List then 1st position")
a = x[-5:-3]
print(a)
print()

print("Last 5 List with [-5-(-3)] = 2 List towards Right")
a = x[-5:-3]
print(a)
print()








