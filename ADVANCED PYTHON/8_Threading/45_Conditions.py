# Condition class is used to improve speed of communication between Threads. The conditions class object is called condition variables. 
# A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: you don't have to track it seperately. 
# A condition is a more advanced version of the evnet object. 


# Create Condition Object ---

# from threading import Condition
# cv = Condition()

# Condition Methods --- 

# 1. notify(n=1) - This method is used to immediately wake up one thread waiting on the condition. Where n is the number of thread need to wake up.

# 2. notify_all() - This method is used to wake up all threads waiting on the condition. 

# 3. wait(timeout=None) - This method wait until notified or until a timeout occurs. if the calling thread has not acquired the lock when this method is called , a RuntimeError is raised. Wait terminates when invokes notify() method or notify_all() method. The return value is True unless a given timeout expired , in which case it is false.


from time import sleep
lst = []

def produce():
    cv.acquire()
    for i in range(1, 6):
        lst.append(i)
        sleep(1)
        print('Item produced.....')
    cv.notify()
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)

cv = Condition()

t1 = Thread(target=produce)
t2 = Thread(target=produce)

t1.start()
t2.start()











