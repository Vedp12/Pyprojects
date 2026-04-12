import asyncio
import time


async def bck_work(n):
    await asyncio.sleep(n)
    print(f"Background job is don after {n}s")


async def main():
    task = asyncio.create_task(bck_work(3))
    time1 = time.time()
    print("Doing another work ... ")
    await asyncio.sleep(2)
    print("Still doning that job")
    print(time.time() - time1)

    await task


asyncio.run(main())
