# SETS TYPE

# Set is an unordered collection of elements much like a set in mathematics.
# The order of elements is not maintained in the sets. It means the element may not appear in the same order as they are entered into the set.

# A set does not accept duplicate elements.
# Set is mutable so we can modify it.
# Sets are undordered so we can not access its element using index.


# # Create Empty set using set() function 

# a = {10, 20, 30, 40, 'Harsh', 'Yadav', 50, 60, 70}
# print(a)
# print(type(a))
# print(id(a))

# b = {10, 20, 30, 40, 'Harsh', 'Yadav', 50, 60, 70, 10, 10, 20, 30}
# print(b)





# # Adding one element 

# x = {10, 20, 'Harsh', 30, 40}
# x.add('Python')
# print(x)



# # Adding Multiple Elements

# y = set()
# y.update([101, 102, 103])
# k = [100, 200, 300]
# y.update(k)
# print(y)




# Deleting Element 

# Remove() method raise an error if element doesn't exist while Discard() method remains unchanged.

r = {10, 20, 30, 40, 'Harsh', 'Yadav', 50, 60, 70}
print("Original Set ", r)
print(id(r))
print()

r.remove('Yadav')
print("After Removing Set ", r)
print(id(r))

r.remove('Sangam')
print("After Removing Set ", r)
print(id(r))

r.discard('Yadav')
print("After Removing Set ", r)
print(id(r))

r.discard('Sangam')
print("After Removing Set ", r)
print(id(r))


# Clear() Method is used to remove all elements to the set

a = {10, 20, 'Harsh', 30, 40, 'Yadav'}
print("Before Clear", a)
print(id(a))
print()

a.clear()

print("After Clear", a)
print(id(a))
















