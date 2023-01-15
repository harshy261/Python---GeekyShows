# LIST COMPREHENSION

# It represent the creation of new list from an iterable object that satisfy a given condition.



# # Normal way ---> 

# # 1 >>>

# lst = [0,1,2,3,4,5,6,7,8,9]
# new_lst = []
# for i in lst:
#     new_lst.append(i+1)
# print(new_lst)



# # 2 >>>

# lst = []
# for i in range(20):
#     lst.append(i+1)
# print(lst)


# # 3 >>>

# lst = []

# for i in range(20):
#     if(i%2==0):
#         lst.append(i)
# print(lst)
# print()



# # 4 >>>

# lst = []

# for i in range(20):
#     if(i%2==0):
#         if(i%3==0):
#             lst.append(i)
# print(lst)
# print()







# # 5 >>>

# lst = []

# for i in range(20):
#     if(i%2==0):
#         lst.append(i)
#     else:
#         lst.append("Invalid")
# print(lst)
# print()
















# List Comprehension way (Conditional) ---> 

# # 1 >>>

# lst1 = [0,1,2,3,4,5,6,7,8,9]
# new_lst1 = [i+1 for i in lst1]
# print(new_lst1)
# print()
# new_lst2 = [i*2 for i in lst1]
# print(new_lst2)



# # 2 >>>

# new_lst = [i+1 for i in range(20)]
# print(new_lst)
# print()

# new_lst1 = [i*3 for i in range(20)]
# print(new_lst1)



# # 3 >>> 

# new_lst = [i for i in range(20) if i%2==0]
# print("New List: ", new_lst)




# # 4 >>> 

# new_lst = [i for i in range(20) if i%2==0 if i%3==0]
# print("New List: ", new_lst)




# # 5 >>> 

new_lst = [i if i%2==0 else "Invalid" for i in range(10)]
print(new_lst)









