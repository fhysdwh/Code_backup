t = ('fhy', 33, True, '山东威海')
print(t)
print(t[0])
print(t[1])

for member in t:
    print(member)

person = list(t)
print(person)

person[1] = 35
print(person)

fruits_list = ['apple', 'orange', 'banana']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
