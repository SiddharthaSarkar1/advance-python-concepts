from multiprocessing import Process
import time


def calculate(n1, n2):
    sum=0
    for i in range(n1, n2):
        sum += i*i


if __name__ == "__main__":

    num = 50_000_000
    mid = num // 2

    p1 = Process(target=calculate, args=(0, mid))
    p2 = Process(target=calculate, args=(mid, num))

    start = time.perf_counter()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()   
    print(f"Time taken: {end - start:,.2f} seconds.")

    print("Bye!")
