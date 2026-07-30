# Multithreading with Function
from threading import Thread
from time import sleep


def hello():
    for i in range(5):
        print(f"Hello, {i+1}")
        sleep(0.5)


def hi():
    for i in range(5):
        print(f"Hi, {i+1}")
        sleep(0.5)


if __name__ == "__main__":

    t1 = Thread(target=hello)
    t2 = Thread(target=hi)

    t1.start()
    sleep(1)
    t2.start()

    # once t1 and t2 completes there work then "Bye!" will be printed
    t1.join()
    t2.join()

    print("Bye!")
