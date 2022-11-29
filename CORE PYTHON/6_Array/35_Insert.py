# Insert Method in Array
#This method is used to insert an element in a particular position of the existing array.


from array import*
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1

print()

print("Array After Insert")
stu_roll.insert(1, 106)
stu_roll.insert(3, 108)

n = len(stu_roll)
i = 0
while(i<n):
    print(stu_roll[i])
    i += 1