# Main Module ----> mainfile


# # SYNTAX 1>>
# import cal

# print("Cal Module's Variable: ", cal.a)
# cal.name()

# add = cal.add(10,20)
# print(add)

# sub = cal.sub(20, 10)
# print(sub)




# # # SYNTAX 2>>
# import cal as c

# print("Cal Module's Variable: ", c.a)
# c.name()

# add = c.add(10,20)
# print(add)

# sub = c.sub(20, 10)
# print(sub)





# # # SYNTAX 3>>
# from cal import a, name, add, sub

# print(a)
# name()
# print( add(10,20) )
# print( sub(20,10) )




# # # SYNTAX 4>>
# from cal import a, name, add as sum, sub as diff

# print(a)
# name()
# print( sum(10,20) )
# print( diff(20,10) )





# # SYNTAX 5>>
from cal import *

print(a)
name()
print( add(10,20) )
print( sub(20,10) )



