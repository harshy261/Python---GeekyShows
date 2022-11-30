# 1-D Numpy Array using Linspace Function

# Linspace function is used to create an array with evenly spaced numbers between a start point and stop point.
# linspace(start, end, num parts, endpoint)   

from numpy import *
a = linspace(2, 8, 4)               # linspace(start, end, parts)
# a = linspace(2, 8, 4, endpoint=False)               # linspace(start, end, parts, endpoint)
print(a)
print(a[0])
print(a[1])
print(a[2])

