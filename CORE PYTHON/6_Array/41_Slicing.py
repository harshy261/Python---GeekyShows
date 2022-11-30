# Slicing in Array
# Slicing on array can be used to retrieve a piece of array that contains a group of element. Slicing is useful to retrieve a range of elements



# 1st Way ----
# from array import*
# stu_roll = array('i',[101,102,103,104,105,106,107,108])
# print("Original Array")
# n = len(stu_roll)
# for i in range(n):
#     print(i, " = " ,stu_roll[i])

# print("**************")

# a = stu_roll[1:5]                     # First to Fifth
# a = stu_roll[1:]                      # First to End
# a = stu_roll[:4]                      # Start to Four
# a = stu_roll[-4:]                     # Last Four
# a = stu_roll[-5:-3]                   # 
# a = stu_roll[0:7:2]                   # start 0 : end 7 : jump 2 step

# for i in a:
#     print(i)

# print("Code Ended")







# 2nd Way -----
from array import*
stu_roll = array('i',[101,102,103,104,105,106,107,108])
print("Original Array")
n = len(stu_roll)
for i in stu_roll[1:5]:
    print(i)










