# CREATING A THREAD BY CREATING CHILD CLASS TO THREAD CLASS 

from threading import Thread

# # 1
# class Mythread(Thread):
#     pass

# t = Mythread()
# print(t.name)




# # 2
# class Mythread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child Thread")

# t = Mythread()
# t.start()

# for i in range(5):
#     print("Main Thread")




# 3
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")

t = Mythread()
t.start()
t.join()
for i in range(5):
    print("Main Thread")




