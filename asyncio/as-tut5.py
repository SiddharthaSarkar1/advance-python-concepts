import asyncio

async def long_operation():
    await asyncio.sleep(5)

async def main():
    try: 
        await asyncio.wait_for(long_operation(), timeout=2)
    except asyncio.TimeoutError:
        print("Operation timed out, took too long ...")


if __name__ == "__main__":
    asyncio.run(main())