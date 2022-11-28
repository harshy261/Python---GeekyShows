# Getting a INPUT in ARRAY by USER

from array import*
stu_roll = array('i',[])
n = int(input("Enter Number of Element: "))

for i in range(n):
    stu_roll.append(int(input("Enter Element: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])
    

