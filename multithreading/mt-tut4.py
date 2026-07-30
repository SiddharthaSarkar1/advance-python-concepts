import threading
import time

def func(seconds):
    print(f"Start: Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Done: Sleeping for {seconds} seconds")

time1 = time.perf_counter()

# func(4)
# func(2)
# func(1)

# Code Using Threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[3])

t1.start()
t2.start()
t3.start()

# Want to wait until the executin of the thread is not complete using join()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)


