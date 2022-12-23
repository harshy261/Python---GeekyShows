# GENERATOR

# Yield Statement - return elements from generator function into a geenrator object.

# next() function
# next(gen_obj)

def disp(a, b):
    yield a
    yield b

result = disp(10, 20)
print(result)
print(type(result))







def disp(a, b):
    yield a
    yield b

result = disp(10, 20)
lst = list(result)
print(lst)
print(type(lst))
print(result)
print(type(result))

print(next(result))
print(next(result))
print(next(result))









def show(a, b):
    while a<=b:
        yield a
        a +=1

result = show(1, 5)
print(result)
print(type(result))

print(next(result))
print(next(result))

for i in result:
    print(i)


















