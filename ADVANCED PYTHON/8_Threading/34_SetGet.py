# SET & GET NAME THREAD NAME

# current_thread()
# getName()
# setName(name)
# name Property


from threading import Thread, current_thread


# # 1
# def disp():
#     print("Child Thread Object", current_thread() )

# t1 = Thread(target=disp)
# t2 = Thread(target=disp)
# t1.start()
# t2.start()

# print("Main Thread", current_thread)




# # 2
# def disp():
#     print("Child Thread Name: ", current_thread().getName() )

# t1 = Thread(target=disp)
# t2 = Thread(target=disp)
# t1.start()
# t2.start()

# print("Main Thread Name: ", current_thread().getName())





# # 3
def disp():
    print("Default Child Thread Name: ", current_thread().getName() )
    current_thread().setName('Doc Thread')
    print("New Child Thread Name: ", current_thread().getName())

t1 = Thread(target=disp)
t1.start()

print("Main Thread Name: ", current_thread().getName())
current_thread().setName('HarshYadav Thread')
print("New Main Thread Name: ", current_thread().getName())


