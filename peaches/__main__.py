import asyncio

from peaches import client


async def async_main():
    bot = client.Peaches()
    try:
        await bot.start()
    finally:
        await bot.close()

asyncio.run(async_main())
