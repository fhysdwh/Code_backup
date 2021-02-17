# class Student(object):
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         print('{}正在上{}课'.format(self.name, course_name))

#     def watchMovie(self):
#         if self.age < 18:
#             print('{}正在观看《小猪佩奇》'.format(self.name))
#         else:
#             print('{}正在偷偷看《苍老师回忆录》'.format(self.name))
    

# s1 = Student('张三', 19)

# s1.study('历史')
# s1.watchMovie()

# class Test:

#     def __init__(self, foo):
#         self.__foo = foo

#     def __bar(self):
#         print(self.__foo)
#         print('__bar')


# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test._Test__bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test._Test__foo)


# if __name__ == "__main__":
#     main()

from time import sleep
import os

class Clock(object):
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
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
        os.system('clear')
        return '%02d : %02d : %02d' % (self._hour, self._minute, self._second)

def main():
    clock = Clock(23, 59, 56)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == "__main__":
    main()
