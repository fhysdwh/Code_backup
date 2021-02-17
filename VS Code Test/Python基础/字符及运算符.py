# a = 100
# b = 1.1
# c = 1 + 5j
# d = 'hello,world'
# e = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# a = int(input('a='))
# b = int(input('b='))
# print('%d + %d = %d' % (a, b, a+b))
# print('%d - %d = %d' % (a, b, a-b))
# print('%d * %d = %d' % (a, b, a*b))
# print('%d / %d = %f' % (a, b, a/b))
# print('%d // %d = %d' % (a, b, a//b))
# print('%d %% %d = %d' % (a, b, a%b))
# print('%d ** %d = %d' % (a, b, a**b))

# a = 10
# b = 3
# a += b
# a *= a + 2
# print(a)

# flag1 = 1 == 1
# flag2 = 3 > 2
# flag3 = 2 < 1
# flag4 = flag1 and flag2
# flag5 = flag1 or flag2
# flag6 = not (1 != 2)
# print('flag1=',flag1)
# print('flag2=',flag2)
# print('flag3=',flag3)
# print('flag4=',flag4)
# print('flag5=',flag5)
# print('flag6=',flag6)

# """
# 将华氏温度转换为摄氏温度
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
# """
# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

# """
# 输入半径计算圆的周长和面积
# """
# r = float(input('请输入圆的半径：'))
# pi = 3.1415926
# zhouchang = 2 * pi * r
# area = pi * r ** 2
# print('圆的周长为{},面积为{}'.format(zhouchang, area))

"""
输入年份 如果是闰年输出True 否则输出False
"""
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)
