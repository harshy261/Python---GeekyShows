# Where() Function - Used to create a new array which contains, returned element chosen from expression1 or expression2 depending on condition.
# If condition is True expression1 is executed else expression2.

# numpy.where(condition, expresasion1, expression2)

from numpy import *

a = array([100,200,300,400,500])
b = array([100,20,30,4000,50])

result = where(a>b, a, b)

print(result)

