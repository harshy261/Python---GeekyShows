# PASSING SET TO FUNCTION

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)

st = {10, 20, 30, 40, 'Harsh', 'Yadav'}
show(st)




# PASSING AND RETURNING SET TO FUNCTION

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s

st = {10, 20, 30, 40, 'Harsh', 'Yadav'}
new_st = show(st)
print(new_st)
print(type(new_st))




