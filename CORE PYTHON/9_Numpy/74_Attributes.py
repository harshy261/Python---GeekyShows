# ATTRIBUTES OF NUMPY ARRAY

# ndim - represent number of dimensions or axes of the array

# shape - represent the shape of array.

# size - represent total number of elements in the array.

# itemsize - represent the memory size of the array element in bytes

# dtype - represent datatype of elements in array

# nbytes - represent total number of bytes occupied by an array


from numpy import *
a = array([101, 202, 303, 404, 505])
b = array(( [10, 20, 30, 40, 50], [60, 70, 80] ))
print()


print("1-D Array ndim : ", a.ndim)
print("2-D Array ndim : ", b.ndim)
print()


print("1-D Array ndim : ", a.shape)
print("2-D Array ndim : ", b.shape)
print()


print("1-D Array ndim : ", a.size)
print("2-D Array ndim : ", b.size)
print()


print("1-D Array ndim : ", a.dtype)
print("2-D Array ndim : ", b.dtype)
print()


print("1-D Array ndim : ", a.nbytes)
print("2-D Array ndim : ", b.nbytes)
print()


print("1-D Array ndim : ", a.itemsize)
print("2-D Array ndim : ", b.itemsize)
print()

