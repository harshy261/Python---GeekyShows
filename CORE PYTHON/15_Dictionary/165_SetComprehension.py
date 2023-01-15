# SET COMPRESHENSION

# It represent the creation of new Set from an iterable object that satisfy a given condition.



# # Normal way ---> 

# # 1 >>>

# set = {0,1,2,3,4,5,6,7,8,9}
# new_set = set()
# for i in set:
#     new_set.add(i+1)
# print(new_set)




# # 2 >>>

# new_set2 = set()
# for i in range(20):
#     new_set2.add(i+1)
# print(new_set2)




# # 3 >>>

# set3 = set()
# for i in range(20):
#     if(i%2==0):
#         set3.add(i)
# print(set3)
# print()



# # 4 >>>

# set4 = set()
# for i in range(20):
#     if(i%2==0):
#         if(i%3==0):
#             set4.add(i)
# print(set4)
# print()



# # 5 >>>

# set5 = set()
# for i in range(10):
#     if(i%2==0):
#         set5.add(i)
#     else:
#         set5.add(i*1000)
# print(set5)
# print()







# # Set Comprehension way -->

# # 1 >>>

# set1 = {0,1,2,3,4,5,6,7,8,9}
# new_set1 = {i+1 for i in set1}
# print(new_set1)
# print(type(new_set1))





# # 2 >>>

# new_set2 = [i+1 for i in range(20)]
# print(new_set2)
# print()
# new_set2 = [i*3 for i in range(20)]
# print(new_set2)



# # 3 >>> 

# new_set3 = [i for i in range(20) if i%2==0]
# print(new_set3)




# # 4 >>> 

# set4 = [i for i in range(20) if i%2==0 if i%3==0]
# print(set4)




# # 5 >>> 

set5 = [i if i%2==0 else i*1000 for i in range(10)]
print(set5)


