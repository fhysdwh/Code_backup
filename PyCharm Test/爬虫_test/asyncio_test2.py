import asyncio
import time

all_start = time.time()
async def test_fun(url):
    start = time.time()
    print('开始访问: ' + url)
    await asyncio.sleep(2)
    print('访问结束!')
    end = time.time()
    run_time = end-start-2
    return run_time

urls = ['www.baidu.com',
        'www.google.com',
        'www.w37fhy.com',
        'www.w37fhy.cn'
        ]

def callback_fun(task):
    print(task.result())
tasks = []
for url in urls:
    c = test_fun(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(callback_fun)
    tasks.append(task)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

all_end = time.time()
print('耗时:' + str(all_end-all_start))