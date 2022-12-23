# Accesing Tuple using For Loop

a = (10, 20, 30, 'GeekyShow')

# Without Index
for element in a:
    print(element)


# With Index
n = len(a)
for i in range(n):
    print(i, " = ", a[i])

