import aiohttp
import asyncio


urls = [
    'https://www.baidu.com',
    'https://www.google.com',
    'https://www.w37fhy.cn',
    'https://www.w37fhy.com'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url, headers=headers) as response:
            page_code = await response.text()
            print(len(page_code))

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
