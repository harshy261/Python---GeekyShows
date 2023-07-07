# Many threads trying to access the same object can lead to problem like making data inconsistent or getting unexpected output. So when a thread is already accessing an object, preventing any other thread accessing the same object is called Thread Synchronization.

# The object on which the threads are synchronized is called Synchronized Object or Mutually Exclusive Lock(mutex).

# Thread Synchronization is recommended when multiple threads are acting on the same object simultaneously.abs
# There are foloowing techniques to do Thread Synchronization:
# 1). Using Locks
# 2). Using RLock(Re-Entrant Lock)
# 3). Using Semaphores



# LOCKS are typically used to synchronize access to a shared resource. Lock can be used to lock the object in which the thread is acting. A lock has only two states, locked and unlocked. It is created in the unlocked state.

# 1. acquire()
# This method is used to change the state to locked and returns immediately. When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked then the acquire() call resets it to locked and returns.

# SYNTAX --- acquire(blocking = True, Timeout = -1)

# True - It blocks until the lock is unlocked , then set it to locked and return True.

# False - It does not block. If a call with blocking is set to True would block, return False immediately; otherwise, set the lock to locked and return False.

# Timeout - When invoked with the floating-point timeout argument set to a positive value, block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired. A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is false.

# The return value is True if the lock is acquired successfully, False if not ( For example if the timeout is expired) 


# 2. release()

# This method is used to release a lock. This can be called from any thread, not only the thread which has acquired the lock.

# When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.

# When invoked on an unlocked lock, a RuntimeError is raised.

# There is no return value.

# SYNTAX --- release()


from threading import * 
import time
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        self.l.acquire(blocking=True, timeout=-1)
        print('Available Seat: ', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
            time.sleep(4)
        else:
            print('Sorry!! All Seats are alloted ')
        self.l.release()

f = Flight(3)
t1 = Thread(target= f.reserve, args=(1,), name='Rahul')
t2 = Thread(target= f.reserve, args=(1,), name='Sonam')
t3 = Thread(target= f.reserve, args=(1,), name='Sangam')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")



