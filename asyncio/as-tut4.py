import asyncio

async def background_task():
    print("Running Background Task ....")
    await asyncio.sleep(5)
    print("Finished Background Task ....")

async def main():
    task = asyncio.create_task(background_task())

    print("Contining immediately in Main")

    await task

    print("But for this we need to wait")


if __name__ == "__main__":
    asyncio.run(main())
    print("Final print statement")

