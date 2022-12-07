# Slicing on 2-D array

# new_arra_name = array_name[start:stop:stepsize, start:stop:stepsize]

from numpy import * 
n = array(( [10,20,30,40], [50,60,70,80], [15,25,35,45] ))

print("Original Array: ")
print(n[0])
print(n[1])
print(n[2])


# print("0th Row All Column")
# a = n[0, :]
# print(a)

# print("1st Row All Column")
# a = n[0, :]
# print(a)

# print("2nd Row All Column")
# a = n[0, :]
# print(a)

# print("All Row 0th Column")
# a = n[:, 0]
# print(a)


# print("All Row 1st Column")
# a = n[:, 1]
# print(a)

# print("All Row 2nd Column")
# a = n[:, 2]
# print(a)


print()
print("Custom Slicing : ")
a = n[0:1, 0:1]
print(a)

print("Custom Slicing : ")
a = n[2:3, 2:3]
print(a)

print("Custom Slicing : ")
a = n[0:2, 1:3]                 # n[rowstart : rowend, colstart : colend]
print(a)





