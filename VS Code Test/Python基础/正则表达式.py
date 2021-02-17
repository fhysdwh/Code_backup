import re

# def main():
#     username = input('请输入您的用户名：')
#     qq = input('请输入您的QQ号：')

#     m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)

#     if not m1:
#         print('请输入有效的用户名！')
    
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('请输入有效的QQ号：')
#     if m1 and m2:
#         print('恭喜你，输入成功！')

# def main():
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     with open('test.txt', 'r') as f:
#         sentence = f.read()
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('--------------华丽的分割线---------------')
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('--------------华丽的分割线---------------')
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
    
# def main():
#     sentence = '你丫的是傻B吗？我操你大爷，Fuck you！'
#     purified = re.sub('[草操肏]|fuck|shit|傻[比逼bB]|煞笔','*',sentence,flags=re.IGNORECASE)
#     print(purified)

def main():
    poem = '床前明月光，疑是地上霜，举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)
    for sentence in sentence_list:
        print(sentence)
    
    








if __name__ == "__main__":
    main()
