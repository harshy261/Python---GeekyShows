# HIGHER ORDER FUNCTION

# map() function 
# map(function_name, iterable)


a = [10, 20, 30, 40, 50]

def inc(n):
    return n+2

result = map(inc, a)
print(result)
print(type(result))






a = [10, 20, 30, 40, 50]

def inc(n):
    return n+2

result = map(inc, a)

for i in result:
    print(i)








a = [10, 20, 30, 40, 50]

def inc(n):
    return n+2

result = list(map(inc, a))
print(result)
print(type(result))
for i in result:
    print(i)











a = [10, 20, 30, 40, 50]

result = list(map(lambda n: n+2, a))

print(result)
print(type(result))
for i in result:
    print(i)











a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

result = list(map(lambda n, m: n+m, a, b))

print(result)
print(type(result))
for i in result:
    print(i)













