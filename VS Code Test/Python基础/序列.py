##### 序列  #######

list1 = [1, 3, 5, 7, 9, 99]
print(list1)
list2 =list1 * 3
print(list2)
print(len(list1), len(list2))

print(list1[1])
print(list2[4])

print(list1[-1])
print(list1[-3])

list1[2] = 300
print(list1)

for index in range(len(list2)):
    print(list2[index])

for elem in list1:
    print(elem)

# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
print('###################')


list1 = [1, 3, 5, 7, 9]

#添加元素,插入元素
list1.append(11)
print(list1)
list1.insert(1, 400)
print(list1)

list1.extend([100, 1000, 10000])
print(list1)
list1 += [1000, 2000]
print(list1) 
print(len(list1))

if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)

list1.pop(0)
print(list1)
list1.pop(len(list1) - 1)
print(list1)

list1.clear()
print(list1)

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2) # apple strawberry waxberry
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2)
list3 = sorted(list1,reverse=True)
print(list3)
list4 = sorted(list1, key=len)
print(list4)
list5 = sorted(list1, key=len, reverse=True)
print(list5)

list1.sort(reverse=True)
print(list1)

l1 = [x for x in range(1, 10)]
print(l1)
l2 = [x * y for x in range(1, 10) for y in range(10, 100, 10)]
print(l2)
l3 = [x + str(y) for x in 'ABCDE' for y in range(1,10)]
print(l3)

import sys

l4 = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(l4))
print(l4)

l5 = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(l5))
print(l5)
for val in l5:
    print(val)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

