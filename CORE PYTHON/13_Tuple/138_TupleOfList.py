# TUPLE OF LIST

a = (10, 20, [30, 40])

print("Original Tuple A : ", a)
print(id(a))
print(type(a))
print


# Modifying Tuple

a[2][0] = 90
print("After Modifying Tuple: ", a)
print(id(a))



# Accessing Tuple of List using For Loop


n = len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])
    else:
        print(i, a[i])