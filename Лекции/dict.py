d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary)# {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←
# типы ключей могут отличатся
print(dictionary['up']) # ↑
# типы ключей могут отличатся
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary:
    print('{}:{}'.format(item, dictionary[item]))
for k,v in dictionary.items():
    print(k,v)
    # up: ↑
    # down: ↓
    # right: →