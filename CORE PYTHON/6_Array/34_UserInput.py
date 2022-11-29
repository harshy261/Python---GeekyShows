# Getting a INPUT in ARRAY by USER using FOR Loop

# from array import*
# stu_roll = array('i',[])
# n = int(input("Enter Number of Element: "))

# for i in range(n):
#     stu_roll.append(int(input("Enter Element: ")))

# for i in range(len(stu_roll)):
#     print(stu_roll[i])
    





# Getting a INPUT in ARRAY by USER using WHILE Loop

from array import*
stu_roll = array('i',[])
n = int(input("Enter Number of Element: "))

i = 0
while(i<n):
    stu_roll.append(int(input("Enter Element: ")))
    i += 1

j = 0
while(j<len(stu_roll)):
    print(stu_roll[j])
    j += 1







