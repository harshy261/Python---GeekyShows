# MULTITASKING

# Process Based Multitasking ---> Where each task is seperate independent program. Suitable for Operating System Level.

# Thread Based Multitasking ----> Where each task is a seperate independent part of the same program. Suitable for Programmatic Level.

# Using Multiple Threads in Program or process

# When we start a Python Program , one thread begins running immediately, which is called Main thread of that program created by PVM.
# Created automatically when program is started.

from threading import Thread


# #1
# def disp():
#     print("Thread Running")

# t = Thread(target = disp)
# t.start()



# #2
# def disp(a, b):
#     print("Thread Running ", a, b)

# for i in range(5):
#     t = Thread(target = disp, args=(10, 20))
    
#     t.start()





# #3
# def disp(a, b):
#     print("Thread Running ", a, b)

# t = Thread(target = disp, args=(10, 20))
    
# t.start()



# #4
# def disp():
#     for i in range(5):
#         print("Child Thread")

# t = Thread(target = disp)

# t.start()

# for i in range(5):
#     print("Main Thread")


# #5
def disp():
    for i in range(5):
        print("Publish video C")

t = Thread(target = disp)

t.start()

for i in range(5):
    print("Publish Video M")


