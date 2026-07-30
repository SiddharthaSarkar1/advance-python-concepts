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
threading.Thread(target=worker, daemon=True, args=("ABC",)).start()
threading.Thread(target=worker, daemon=True, args=("XYZ",)).start()

input(f"Press Enter to stop: \n")
done = True
