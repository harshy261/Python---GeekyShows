# Two or more threads communicate with each other.
# 1. Event
# 2. Condition
# 3. Queue


# EVENT --- 
# This is one of the simplest mechanism for communication between threads:
# one thread signals an event and other threads wait for it.

# An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true. 
# The flag is initially false.

# Create Event Object ----
# from threading import Event
# e = Event()

# EVENT METHODS ----

# 1. set() - It sets the internal flag to true. All threads waiting for it to become true are awakened. Threads that call wait() once the flag is true will not block at all. 

# 2. clear() - It resets the internal flag to false. Subsequently, threads calling wait() will block until set() is called to set the internal flag to true again. 

# 3. is_set() - It returns true if an only if the internal flag is true.

# 4. wait(timeout=None) - It blocks until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, block until another thread calls set() to set the flag to true, or until the optional timeout occurs.





from threading import Thread, Event
from time import sleep

def light_switch():
    sleep(3)
    e.set()
    print('Green Light On')
    sleep(5)
    print('Red Light On')
    e.clear()

def traffic():
    e.wait()
    while e.is_set():
        print('You can Go.....')
        sleep(.5)
    print('Program Done ')

e = Event()
t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)
t1.start()

