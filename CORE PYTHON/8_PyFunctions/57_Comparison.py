# Comapring Arrays

# Size of array must be same. Compares corresponding elements of the arrays and return another array with boolean value.

from numpy import *

a = array([100,200,300,400,500])
b = array([100,200,300,400,50])

result = a == b
print(result)
print()

result = a < b
print(result)
print()

result = a > b
print(result)
print()

