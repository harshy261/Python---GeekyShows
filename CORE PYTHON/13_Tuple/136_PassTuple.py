# PASSING TUPLE TO FUNCTION

def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)

tuple = (10, 20, 30, 40, 'HARSH')
show(tuple)







# RETURNING TUPLE TO FUNCTION

def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t

tuple = (10, 20, 30, 40, 'HARSH')
new_tup = show(tuple)
print(new_tup)
print(type(new_tup))





