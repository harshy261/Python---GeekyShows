# HIGHER ORDER FUNCTION

# filter() function - filter out elements of an iterable (sequence) depending on a function that test each element in the sequence to be true or not.
# filter(function_name, iterable) 


a = [10, 20, 30, 40, 50, 60, 70, 80]

def high_marks(n):
    if n>=60:
        return True

result = filter(high_marks, a)
print(result)
print(type(result))

for i in result:
    print(i)


# Converting into list
result = list(filter(high_marks, a))
print(result)
print(type(result))

for i in result:
    print(i)





a = [10, 20, 30, 40, 50, 60, 70, 80]

result = list(filter(lambda n: (n>=60), a))
print(result)
print(type(result))

for i in result:
    print(i)







a = [True, False, False, True, False, True, True]

result = list(filter(None, a))
print(result)
print(type(result))

for i in result:
    print(i)







