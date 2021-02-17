# from random import randint
# from time import time, sleep

# def download_task(filename):
#     print('开始下载{}....'.format(filename))
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('{}下载完成！耗费了{}秒'.format(filename, time_to_download))

# def main():
#     start = time()
#     download_task('python教程')
#     download_task('java教程')
#     end = time()
#     print('全部下载完毕，共耗费了{}秒'.format(str(end - start)))

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

# def download_task(filename):
#     print('启动下载进程，进程号{}'.format(getpid()))
#     print('开始下载{}'.format(filename))
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('{}下载完成！耗费了{}秒'.format(filename, time_to_download))

# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python教程.rar', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Java教程.zip', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#      print('下载全部结束，共耗费了{}秒'.format(end - start))
# from threading import Thread

# def download_task(filename):
#     print('开始下载{}'.format(filename))
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('{}下载完成，共耗费了{}秒'.format(filename,time_to_download))

# def main():
#     start = time()
#     t1 = Thread(target = download_task, args=('Python',))
#     t1.start()
#     t2 = Thread(target= download_task, args=('java', ))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('共耗费了{}秒'.format(end - start))

from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()
    
    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()
    
    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：¥ {}元'.format(account.balance))




if __name__ == "__main__":
    main()



