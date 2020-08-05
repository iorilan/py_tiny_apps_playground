

"""
    pip install aiohttp
"""
import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def open_url(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print(len(html))

async def open_all():
    urls = ["https://github.com/iorilan"]*50

    start = time.time()
    for url in urls:
        await open_url(url)
    
    end = time.time()
    print(f'open {len(urls)} url .time used {round(end-start,2)} second')

if __name__ == "__main__":
    
    asyncio.get_event_loop().run_until_complete(open_all())

    

    