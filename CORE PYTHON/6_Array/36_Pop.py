# POP Method in Array
#This method is used to remove an element in a existing array.


# from array import*
# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while(i<n):
#     print(stu_roll[i])
#     i += 1

# print()

# print("Array After POP")
# stu_roll.pop()
# stu_roll.pop()

# n = len(stu_roll)
# i = 0
# while(i<n):
#     print(stu_roll[i])
#     i += 1






#This method is used to pop an element from specified position in a existing array.

from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1

print()

print("Array After POP")
r = stu_roll.pop(1)
print("Removed Element: ", r)

n = len(stu_roll)
print("Number of element remaining",n)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1








