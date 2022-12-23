# Slicing Tuple

x = (101, 102, 103, 104, 105, 106, 107)
print("Original Tuple")

n = len(x)
for i in range(n):
    print(i, "=", x[i])
print()

print("From 1st Position to 4th Position")
a = x[1:5]
for i in a:
    print(i)
print()

print("From 0th Position to last Position")
b = x[0:]
for i in b:
    print(i)
print()




























