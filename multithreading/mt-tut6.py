import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Start: Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Done: Sleeping for {seconds} seconds")
    return seconds

# thread pooling demo using map
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)


poolingDemo()
