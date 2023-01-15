# DICTIONARY COMPREHENSION


# # Normal way ---> 

# # 1 >>>

# dict1 = {}
# for n in range(10):
#     dict1[n] = n*2
# print(dict1)


# # 2 >>>

# dict2 = {}
# for n in range(20):
#     if(n%2==0):
#         dict2[n] = n*2
# print(dict2)
# print()



# # 3 >>>

# dict3 = {}
# for n in range(20):
#     if(n%2==0):
#         if(n%3==0):
#             dict3[n] = n*2
# print(dict3)
# print()




# # 4 >>>

dict4 = {}
for n in range(20):
    if(n%2==0):
        dict4[n] = n
    else:
        dict4[n] = "Invalid"
print(dict4)
print()







# # Set Comprehension way -->

# # 1 >>>

# dict1 = { n:n*2 for n in range(10) }
# print(dict1)




# # 2 >>> 

# new_dict2 = {n:n*2 for n in range(10) if n%2==0}
# print(new_dict2)



# # 3 >>> 

# new_dict3 = {n:n*2 for n in range(10) if n%2==0 if n%3==0}
# print(new_dict3)



# # 4 >>> 

new_dict4 = {n:(n if n%2==0 else 'Invalid') for n in range(10) }
print(new_dict4)



# CONVERT LIST TO DICTIONARY ----> 

lst = [ (101, "Harsh"), (102, "Raj") ]

dict = {k:v for k, v in lst }




