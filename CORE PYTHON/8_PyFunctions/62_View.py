# VIEW method 

# used to construct a new view of array with same data of existing array. The existing array and a new array will share different memory locations.

# The existing array and new array will share different memory locations.

# If the new array get modified, the existing will also be modified as the elements in both the array will be like mirror image.


from numpy import *

a = array([10, 20, 30, 40, 50])
b = a.view()

a[1] = 80
b[2] = 300 

print(a)
print(b)

print("a", id(a))
print("b", id(b))


