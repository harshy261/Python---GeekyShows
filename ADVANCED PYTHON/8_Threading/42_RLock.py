# A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread.abs
# The Standard Lock doesn't know which thread is currently holding the lock. If the lock is held, any thread that attempts to acquire it will block, even if the same thread itself is already holding the lock. In such cases, RLock(reentrant lock) is used.

# A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it.


from threading import * 
import time
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        # print(self.l)

    def reserve(self, need_seat):
        self.l.acquire(blocking=True, timeout=-1)
        self.l.acquire(blocking=True, timeout=-1)
        print(self.l)
        print('Available Seat: ', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
            # time.sleep(4)
        else:
            print('Sorry!! All Seats are alloted ')
        self.l.release()
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



