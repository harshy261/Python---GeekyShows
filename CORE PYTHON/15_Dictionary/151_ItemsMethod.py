# ITEMS METHOD 

# This method returns an object that contains key-value pairs of dictionary.
# The pairs are stored as tuples in the object.


stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print()

it = stu.items()
print(it)
print(type(it))




# Accessing the elements

lst = list(it)
print(lst)
print(type(lst))
print()


print(lst[0])
print(lst[1])
print(lst[2])

print(lst[0][1])



for r in lst:
    for c in r:
        print(c)


