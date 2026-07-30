import asyncio
import time

async def io_task(name, delay, n_iter):
    for i in range(1, n_iter+1):
        print(f"Name: {name} -> Iteration: {i}")
        await asyncio.sleep(delay) # await asyncio.sleep(delay) -> yield back to the event loop


async def main():
    start = time.perf_counter()
    await asyncio.gather(
        io_task("Task A", 1, 3),
        io_task("Task B", 2, 3),
        io_task("Task C", 3, 3),
    )
    end = time.perf_counter()
    print(f"Total time: {end-start}")

    start = time.perf_counter()
    await io_task("Task A", 1, 3),
    await io_task("Task B", 2, 3),
    await io_task("Task C", 3, 3),
    end = time.perf_counter()
    print(f"Total time: {end-start}")

asyncio.run(main())

# Name: Task A -> Iteration: 1
# Name: Task B -> Iteration: 1
# Name: Task C -> Iteration: 1
# Name: Task A -> Iteration: 2
# Name: Task B -> Iteration: 2
# Name: Task A -> Iteration: 3
# Name: Task C -> Iteration: 2
# Name: Task B -> Iteration: 3
# Name: Task C -> Iteration: 3
# Total time: 9.008364961999632
# Name: Task A -> Iteration: 1
# Name: Task A -> Iteration: 2
# Name: Task A -> Iteration: 3
# Name: Task B -> Iteration: 1
# Name: Task B -> Iteration: 2
# Name: Task B -> Iteration: 3
# Name: Task C -> Iteration: 1
# Name: Task C -> Iteration: 2
# Name: Task C -> Iteration: 3
# Total time: 18.02103224600023