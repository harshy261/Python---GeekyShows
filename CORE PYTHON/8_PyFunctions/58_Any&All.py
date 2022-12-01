# Any() function - returns true, if any one element of the iterable is True. If iterable is empty then returns False.

# All() function - returns True , if all elements of the iterable are True or iterable is Empty.

# These are Pythons Built-in Function.


from numpy import *

a = array([100,200,300,400,500])
b = array([100,200,300,400,50])

result = a == b
print(result)
print(any(result))
print(all(result))






