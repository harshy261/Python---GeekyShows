# PASSING DICTIONARY TO FUNCTION

def show(d):
    print(d)
    print()
    print(type(d))
    for k in d:
        print(k, '=', d[k])

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}

show(dc)



# Returning Dictionary 

def show(d):
    print(d)
    print()
    print(type(d))
    for k in d:
        print(k, '=', d[k])
    return d

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}

new_dc = show(dc)
print(new_dc)
print(type(new_dc))









