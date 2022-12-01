# 1-D Numpy Array using Logspace Function

# Logspace function is used to create an array with evenly spaced numbers logarithmically. The sequence start at base** start (base to the power of start) and ends with base** stop.


# numpy.logspace(start, stop, num = 50, endpoint= True, base = 10.0, dtype = None, axis = 0)

from numpy import * 
a = logspace(2, 10, 5, base = 2)
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
