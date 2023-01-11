# LIST OF TUPLES

a = [10, 20, (30, 40)]
print("Original List")
print(id(a))
print(type(a))
print

# Appending a new Tuple 
a.append((50, 60))
print("After Appending a Tuple : ")
print(id(a))
print(type(a))
print()


# Accessing List of Tuple using For Loop

n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])
    else:
        print(i, a[i])

