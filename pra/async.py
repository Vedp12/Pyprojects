"""
Event LOOP
CoRoutine
Tasks
Futures
gather
TaskGroup
"""

import asyncio


async def fetch_data(delay, id):
    print("Fetching id data", id)
    await asyncio.sleep(delay)
    print("Data fetched of ID", id)
    return f"ID: {id}"


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([3, 2, 5], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    results = [task.result() for task in tasks]
    for result in results:
        print(f"Received data: {result}")


asyncio.run(main())
