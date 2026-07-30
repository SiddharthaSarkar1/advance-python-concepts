import threading
import time

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

# We are using a thread to run the worker function
threading.Thread(target=worker).start()

input(f"Press Enter to stop: \n")
done = True
