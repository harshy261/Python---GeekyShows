# Accessing Array using FOR LOOP


# 1st Way ---
# from array import*
# stu_roll = array('i',[101,102,103,104,105])

# for element in stu_roll:
#     print(element)





# 2nd Way ---
from array import*
stu_roll = array('i',[101,102,103,104,105])

n = len(stu_roll)
print(n)
print()
for i in range(n):
    print("index",i, " = " ,stu_roll[i])






