# def main():
#     s1 = 'hello,world'
#     s2 = "hello,world"
#     s3 = """
#     hello,world
#     I am Fhy
#     """

#     print(s1, s2, s3)

#     s1 = r'\'Hello,World\''
#     s2 = r'\n\\hello,world!\\\n'
#     print(s1, s2, end='')

#     s1 = '\141\142\143\x61\x62\x63'
#     s2 = '\u9a86\u660a'
#     print(s1, s2)

# if __name__ == "__main__":
#     main()


s1 = 'hello' * 3
print(s1)

s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
print(str2[2])

print(str2[2 : 5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])

str1 = 'hello,world'

print(len(str1))

#字符串首字母大写
print(str1.capitalize())
#字符串中每个单词首字母大写
print(str1.title())
#字符串 全部变为大写
print(str1.upper())
#查找子字符串的位置
print(str1.find('or'))
#检查字符串是否以指定的字符串开头
print(str1.startswith('he'))
print(str1.startswith('hello '))

#检查字符串是否以指定的字符串结尾
print(str1.endswith('d'))
print(str1.endswith('d!'))

#字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50,'*'))
#字符串以指定的宽度靠右放置并在左侧填充指定的字符
print(str1.rjust(50,' '))

str2 = 'abc12354556'

#检查字符串是否由数字构成
print(str2.isdigit())
#检测字符串是否由字母构成
print(str2.isalpha())
#检查字符串是否由数字和字母构成
print(str2.isalnum())

str3 = '    afly@1.com'
print(str3)
print(str3.strip())


a, b = 5, 10

print('{} * {} = {}'.format(a, b, a * b))

print(f'{a} * {b} = {a * b}')



