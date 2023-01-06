# Accesing Tuple using While Loop

a = (10, 20, 30, 'GeekyShow')

# Without Index
for element in a:
    print(element)


# With Index
n = len(a)
i=0
while i<n:
    print(a[i])
    i+=1

