# RESHAPE ARRAY

# This is used to change the shape of array. 
# We can convert the 2-D or 3-D array to 1-D or vice versa.

# x = reshape(array_name, row, column)

from numpy import *

# Converting 1-D to 2-D :-

a = array([1, 2, 3, 4, 5])
b = reshape(a, (2, 3))
print(b)


# Converting 1-D to 3-D :-
x = array([1, 2, 3, 4, 5])
y = reshape(x, (2, 3, 2))
print(y)


# Converting 2-D to 1-D :-

g = array([ [1,2,3], [4,5,6] ])
h = reshape(g, (6))





