import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Start: Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Done: Sleeping for {seconds} seconds")

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 5)
        print(future1.result())
        print(future2.result())
        print(future3.result())


poolingDemo()
