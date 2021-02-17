# from time import time
# from threading import Thread

# import requests

# class DownloadHanlder(Thread):

#     def __init__(self, url):
#         super().__init__()
#         self.url = url
    
#     def run(self):
#         #http://image.hnol.net/c/2019-03/20/11/201903201131027731-239867.jpg
#         #从右边开始找第一个/后面的字符串为 文件名。
#         filename = self.url[self.url.rfind('/') + 1:]
#         resp = requests.get(self.url)
#         with open('./girls/' + filename, 'wb') as f:
#             f.write(resp.content)

# def main():
#     resp = requests.get(
#         'http://api.tianapi.com/meinv/?key=9da9e045f6a43a1c0866ddd0a609b4e6&num=10'
#     )
#     date_model = resp.json()
#     for mm_dict in date_model['newslist']:
#         url = mm_dict['picUrl']
#         DownloadHanlder(url).start()

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    server = socket(family= AF_INET, type= SOCK_STREAM)
    server.bind(('192.168.50.113', 6789))
    server.listen(512)
    print('服务器已启动，开始监听....')

    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器！')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()






if __name__ == "__main__":
    main()
