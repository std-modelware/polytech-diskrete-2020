# Словарь - набор ключей и значений
# Начиная с Python 3.6 ключи сортируются по порядку вставки

info = {'key1': 'value1', 'key2': 'value2'}
print(info)

info2 = dict([('key1', 'value1'), ('key2', 'value2')])
print(info2)

info['key3'] = 3
print(info)

info['key1'] = 1
print(info)

print(info['key2'])

# print(info['key4']) # ошибка

if 'key4' in info:
    print(info['key4'])
else:
    print('no such value')

value4 = info.get('key4', 'no value')
print(value4)

# удаление элемента из словаря по ключу
del info['key1']
print(info)

# перебор ключей (1)
for key in info:
    print(key)
    # del info[key] # нельзя

# перебор ключей (2)
# возвращается представление (view) - указывает на РЕАЛЬНЫЕ ключи, а не на их копии
keys = info.keys()
for key in keys:
    print(key)

# перебор значений
# возвращается представление (view) - указывает на РЕАЛЬНЫЕ значения, а не на их копии
values = info.values()
for value in values:
    print(value)

# Удаление реального значения ведет к удалению из keys() и values()
del info['key2']

print(keys)
print(values)

for key, value in info2.items():
    print(key, value)