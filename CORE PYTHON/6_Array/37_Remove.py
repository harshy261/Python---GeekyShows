# REMOVE Method in Array
# This method is used to remove first occurence of an element in a existing array. If it doesn't found the element, shows valueError.


from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1


print()


print("Array After REMOVE")
r = stu_roll.remove(101)
print("Removed Element: ", r)

n = len(stu_roll)
print("Number of element remaining",n)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1