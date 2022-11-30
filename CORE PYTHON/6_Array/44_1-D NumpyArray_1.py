# 1-D Numpy Array using Array Function

# array() function
# linspace() function
# logspace() function
# arange() function
# zeros() function
# ones() function




# 1st WAY ----

import numpy
stu_roll = numpy.array([101,102,103,104,105])
# stu_roll = numpy.array([101,102,103,104,105], dtype= float)       # explicitly convert into FLOAT
# stu_roll = numpy.array(['a','b','c','d','e'])

print(stu_roll)
print(stu_roll.dtype)

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])




# 2ND WAY ----

from numpy import *
stu_roll = array([101,102,103,104,105])
# stu_roll = numpy.array([101,102,103,104,105], dtype= float)       # explicitly convert into FLOAT
# stu_roll = numpy.array(['a','b','c','d','e'])

print(stu_roll)
print(stu_roll.dtype)

stu_roll[1] = 110

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])







