from threading import Thread
import time


def calculate(n1, n2):
    sum=0
    for i in range(n1, n2):
        sum += i*i


if __name__ == "__main__":

    num = 50_000_000
    mid = num // 2

    t1 = Thread(target=calculate, args=(0, mid))
    t2 = Thread(target=calculate, args=(mid, num))

    start = time.perf_counter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()   
    print(f"Time taken: {end - start:,.2f} seconds.")

    print("Bye!")
