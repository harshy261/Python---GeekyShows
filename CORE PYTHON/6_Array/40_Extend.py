# EXTEND Method in Array
# This method is used to append another array or iterable object at the end of the array.


from array import*
stu_roll = array('i',[101,102,103,104,105])
arr = array('i', [107,108,109,110])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1

print()

print("Array After Extend")
stu_roll.extend(arr)

n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1



