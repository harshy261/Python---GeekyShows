# DAEMON THREAD ----

# A daemon thread is a thread which runs continously in the background.
# It provide support to non-daemon threads

# When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not requirred to terminate daemin thread explicitly. 


# CREATE DAEMON THREAD ---- 

# setDaemon(True) Method or daemon = True Property is used to make a thread Daemon thread.

# Ex --
# t1 = Thread(target = disp)
# t1.setDaemon(True)
# t1.Daemon = True
# t1.Daemon = False


from threading import Thread 
def disp():
    print('Daemon Thread')

t1 = Thread(target=disp)
print('Before: ', t1.isDaemon())
t1.setDaemon(True)
t1.start()
print('After: ', t1.isDaemon())
# t1.start()


# Main Thread is always non-Daemon Thread

# Rest of the threads inherit daemon nature from their parents. 
# - If parent thread is non daemon then the child thread will become non daemon thread.
# - If parent thread is daemon then the child thread will become daemon thread.

# When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not requirred to terminate daemon thread explicitly. 











