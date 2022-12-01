# NonZeros() Function - Used to determine the positions of elements which are non zero. Returns an array that contains the indexes of the element of the array which are not equal to zero.


from numpy import *

a = array([1, 25, 0, 3, 40, 0, 50])
result = nonzero(a)
print(result)



