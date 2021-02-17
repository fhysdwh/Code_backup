# class Person(object):

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def age(self):
#         return self._age

#     @age.setter

#     def age(self,age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('{}正在玩五子棋'.format(self._name))
#         else:
#             print('{}正在玩扎金花'.format(self._name))

# def main():
#     person = Person('禾禾', 3)
#     print(person.name)
#     print(person.age)
#     person.play()
#     person.age = 17
#     person.play()

# if __name__ == "__main__":
#     main()



# class Person(object):

#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ('_name', '_age', '_gender')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()