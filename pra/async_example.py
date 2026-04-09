import asyncio


async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)  # Simulate I/O delay
    print(f"Goodbye, {name}!")


# Run the coroutine
asyncio.run(greet("Ved"))
