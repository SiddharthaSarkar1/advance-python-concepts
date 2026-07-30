import threading
import time

done = False

def worker(text):
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(f"{text}: {counter}")

# We are using a thread to run the worker function, we are also setting the daemon to True
t1 = threading.Thread(target=worker, daemon=True, args=("ABC",))
t2 = threading.Thread(target=worker, daemon=True, args=("XYZ",))

t1.start()
t2.start()

t1.join()
t2.join()

input(f"Press Enter to stop: \n")
done = True
