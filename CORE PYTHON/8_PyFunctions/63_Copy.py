# COPY method

# used to create a copy of an existing array. If the new array got modified, the existing array will not be affected or vice versa. Both the arrays are independent.

from numpy import *

a = array([10, 20, 30, 40, 50])
b = copy(a)

print(a)
print(b)

print("a", id(a))
print("b", id(b))


