# One Dimensional Array

# Ways to Import array :
# 1. import array
# 2. from array import *



# 1st way ---
import array
stu_roll = array.array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])


# 2nd way ---
import array as arr
stu_roll = arr.array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])



# 3rd Way ---
from array import*
stu_roll = array('i',[101,102,103,104,105])
stu_marks = array('f',[1.01,1.02,1.03,1.04,1.05])
stu_num = array('i',[1,1,1.03,1,1.05])      # implicit type conersion of int to float

print(stu_roll[0])
print(stu_roll[1])

print(stu_marks[0])
print(stu_marks[1])


print(stu_num[0])
print(stu_num[1])
print(stu_num[2])
print(stu_num[3])





# Creating Empty 1-D array

from array import*
stu_roll = array('i',[])            # i for int, f for float, b for char





