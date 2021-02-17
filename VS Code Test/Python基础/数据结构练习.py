# # 字符串 跑马灯效果～
# import os
# import time

# def main():
#     content = '北京欢迎你，为你开天辟地....'
#     while True:
#         os.system('clear')
#         print(content)
#         time.sleep(0.6)
#         content = content[1:] + content[0]

# if __name__ == "__main__":
#     main()

# #生成验证码

# import random

# def generate_code(code_len = 4):
#     all_chars = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
    
#     return code

# print(generate_code(8))

        
# # 返回文件名的后缀

# def get_houzhui(filename, has_dot = False):
#     pos = filename.rfind('.')
#     print(pos)

#     if 0 < pos < len(filename) -1:
#         index = pos if has_dot else pos+1
#         print(index)
#         return filename[index:]
#     else:
#         return ''

# print(get_houzhui('aaaa.exe', True))

# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2

# print(max2([1,3,5,33,2,6,76,423,87]))

# #双色球选号
# from random import randrange, randint, sample


# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')

#         print('%02d' % ball, end=' ')
#     print()


# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     #random模块的sample函数来实现从列表中选择不重复的n个元素。
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls


# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())


# if __name__ == '__main__':
#     main()

#井字棋游戏
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()