import asyncio
import time

async def test_fun(url):
    print('开始访问: ' + url)
    time.sleep(2)
    print('访问结束!')
    return url


c = test_fun('www.w37fhy.cn')


def callback_fun(task):
    print(task.result())


loop = asyncio.get_event_loop()
# task = loop.create_task(c)
task = asyncio.ensure_future(c)
task.add_done_callback(callback_fun)
loop.run_until_complete(task)

