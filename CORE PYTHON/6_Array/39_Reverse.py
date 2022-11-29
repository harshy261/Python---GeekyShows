# REVERSE Method in Array
# This method is used to reverse the order of elements in the array.


from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1

print()

print("Array After REVERSE")
stu_roll.reverse()

n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1