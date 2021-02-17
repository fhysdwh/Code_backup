# def main():

#     f = open('test.txt', 'r', encoding='utf-8')
#     print(f.read())
#     f.close()

# if __name__ == "__main__":
#     main()


# def main():
#     f = None
#     try:
#         f = open('test.txt', 'r', encoding = 'utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定文件！')
#     except LookupError:
#         print('指定了未知编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#     finally:
#         if f:
#             f.close()
# import time

# def main():
#     #一次性读取
#     with open('test.txt', 'r', encoding = 'utf-8') as f:
#         print(f.read())
#     #通过for-in循环逐行读取
#     with open('test.txt', mode = 'r') as f:
#         for line in f:
#             print(line, end = '')
#             time.sleep(0.5)
#     print('##########')

#     #读取文件按行读取到列表中   
#     with open('test.txt', 'r', encoding = 'utf-8') as f:
#         lines = f.readlines()
#         for line in lines:
#             line = line.strip('\n')
#             print(line)
#     print(lines)

# from math import sqrt

# def is_prime(n):
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False

# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding = 'utf-8'))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误！')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成！')

# def main():
#     try:
#         with open('1.jpg', 'rb') as pic1:
#             data = pic1.read()
#             print(type(data))
#         with open('2.jpg','wb') as pic2:
#             pic2.write(data)
#     except FileNotFoundError as e:
#         print('打不开指定文件！')
#     except IOError as e:
#         print('读写文件出错！')

import json

def main():
    mydict = {
        'name' : 'fhy',
        'age' : 34,
        'qq' : 77025494,
        'friends' : ['张三', '李四'],
        'cars' : [
            {'brand' : 'BYD', 'max_speed' : 180},
            {'brand' : 'Audi', 'max_speed' : 280},
            {'brand' : 'Benz', 'max_speed' : 320},
        ]    
    }
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            newdict = json.load(f)
    except IOError as e:
        print(e)
    print(newdict)
    print('保存读取完成')


if __name__ == "__main__":
    main()

