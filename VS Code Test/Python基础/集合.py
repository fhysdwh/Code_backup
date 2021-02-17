set1 = {1, 2, 3, 4, 5, 6, 7}
print(set1)
print('length=', len(set1))

set2 = set(range(1, 10))
set3 = set((1, 2, 3, 4, 5, 6, 7, 8))
print(set2, set3)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(14)
set1.add(15)

set2.update([11, 12])

set2.discard(5)

print(set1)
print(set2)

print(set3.pop())
print(set3)
print('######################')
s1 = {1, 2, 3, 4, 5, 10, 20}
s2 = {10, 20, 30, 3, 4, 5, 6}

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)

s3 = {1,2,3,4,5,6,7,10,20,30,40}

print(s1 <= s2)
print(s1 >= s2)
print(s1 <= s3)
print(s2 <= s3)
