scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}

print(scores)

i1 = dict(one = 1, two = 2, three = 3, four = 4)
print(i1)

i2 = dict(zip(['a', 'b', 'c'], '1234'))
print(i2)

i3 = {num : num ** 2 for num in range(1, 10)}
print(i3)

print(scores['狄仁杰'])

for key in scores:
    print('{} = {}'.format(key, scores[key]))


scores['狄仁杰'] = 88
scores.update(禾禾 = 100, 涵涵 = 1)
print(scores)

if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
print(scores.get('武则天', 60))
print(scores)
print(scores.popitem())
print(scores)
print(scores.pop('禾禾', 100))
print(scores)

scores.clear()
print(scores)



