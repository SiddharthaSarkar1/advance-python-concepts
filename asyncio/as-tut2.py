import asyncio

async def main():
    task = asyncio.create_task(other_func())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(f"Return value from other_func(): {return_value}")

async def other_func():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return "Other function completed successfully!"

asyncio.run(main())