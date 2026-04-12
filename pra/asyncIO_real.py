import asyncio


async def slow_task():
    await asyncio.sleep(2)
    return "finished"


async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=10.0)
        print(result)
    except asyncio.TimeoutError:
        print("Task took too long — cancelled!")


asyncio.run(main())
