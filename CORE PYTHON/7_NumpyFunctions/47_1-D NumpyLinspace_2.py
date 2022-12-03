
# ACCESSING ARRAY USING FOR LOOP

# from numpy import *
# a = linspace(2, 8, 4)


# # 1st Way ----
# for element in a:
#     print(element)


# # 2nd Way ----
# n = len(a)
# print(n)

# for i in range(n):
#     # print(stu_roll[i])
#     print('index', i, "=", a[i])






# ACCESSING ARRAY USING WHILE LOOP


from numpy import *
a = linspace(2, 8, 4)

n = len(a)
print(n)

i = 0
while i<n :
    print("index", i, "=",a[i])
    i+=1








