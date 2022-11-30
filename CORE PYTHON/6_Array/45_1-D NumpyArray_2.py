# ACCESSING ARRAY USING FOR LOOP

# from numpy import *
# stu_roll = array([101,102,103,104,105])


# # 1st Way ----
# for element in stu_roll:
#     print(element)


# # 2nd Way ----
# n = len(stu_roll)
# print(n)

# for i in range(n):
#     # print(stu_roll[i])
#     print('index', i, "=", stu_roll[i])








# ACCESSING ARRAY USING WHILE LOOP


from numpy import *
stu_roll = array([101,102,103,104,105])

n = len(stu_roll)
print(n)

i = 0
while i<n :
    print("index", i, "=",stu_roll[i])
    i+=1










