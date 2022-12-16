# SLICING ON THE LIST       --  retrieve a piece of list  

# used to retrieve the range of elements

# new_list_name = list_name[start:stop:stepsize]


a = [10, 20, 30, 40, 50, 60, 70, 80]

print("Original List")
n = len(a)
for i in range(n):
    print(i, " = ", a[i])
print()

print("From 1st to 4rth Position")
x = a[1:5]
for i in x:
    print(i)
print()

print("From 0th to last Position")
y = a[0:]
for i in y:
    print(i)
print()


print("From 0th to 4rth Position")
z = a[:5]
for i in z:
    print(i)
print()


print("Last 4 Elements")
k = a[-4:]
for i in k:
    print(i)
print()


print("From 0th to 6th Position stride 2")
l = a[0:7:2]
for i in l:
    print(i)
print()


print("Last 5 Elements with [-5-(-3)] = 2 elements towards right")
f = a[-5:-3]
for i in f:
    print(i)
print()












