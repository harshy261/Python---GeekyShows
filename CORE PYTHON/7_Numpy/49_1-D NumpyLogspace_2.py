# ACCESSING ARRAY USING FOR LOOP

from numpy import *
a = logspace(2, 10, 5, base = 2)


# # 1st Way ----
# for element in a:
#     print(element)


# 2nd Way ----
n = len(a)
print(n)

for i in range(n):
    # print(stu_roll[i])
    print('index', i, "=", a[i])
    





