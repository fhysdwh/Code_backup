# sum = 0 
# for x in range(101):
#     sum += x

# print(sum)


# newsum = 0
# for x in range(0, 101, 2):
#     newsum += x
# print(newsum)
# import random
# x = random.randint(0, 11) 
# count = 0
# while True:
#     count += 1
#     y = int(input('y='))
#     if y > x:
#         print('大了')
#     elif y < x:
#         print('小了')
#     else :
#         print('恭喜你答对了,一共猜了{}次'.format(count))
#         break

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{} * {} = {}'.format(i, j, i * j),end='\t')
#     print('',end='\n')   

# for i in range(1, 6):
# #     for j in range(1, i + 1):
# #         print('*',end='')
# #     print('',end='\n')    

# row = int(input('请输入行数：'))
# # for i in range(1, row + 1):
# #     for j in range(1, row + 1 - i): 
# #         print(' ',end='')
# #     for g in range(1, i + 1):
# #         print('*',end='')
# #     print('',end='\n')    

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()