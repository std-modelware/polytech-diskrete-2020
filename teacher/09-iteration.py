# Итерации

name = list('ALEX')

for letter in name:
    print(letter)

for letter in list('ALEX'):
    print(letter)

for letter in ['A', 'L', 'E', 'X', '!']:
    print(letter)

# переменная сохраняет последнее значение
print(letter)

# перебор с индексом
# результат от применения enumerate - tuple (кортеж)
for data in enumerate(name):
    print(data)

for index, item in enumerate(name):
    print(index, item)

# пропуск и ранний выход из цикла
data = list(range(10)) + list(range(0, -10, -1))
print(data)

for index, item in enumerate(data):
    if index % 2 == 0:
        continue

    # if item < 0:
    #     break

    print(index, item)
else:
    # не заходим в эту секцию, если вышли по break
    print('else')

# принадлежность списку
print(12 in data)
print(-2 in data)

# Удаление элементов из списка
# Когда python проходит по циклу, он "думает", что список меняться НЕ будет и он ориентируется на index
print(data)
for item in data:
    if item < 0:
        data.remove(item)
#    print(data)

print(data)

# перебор делать по копии
for item in data[:]:
    if item < 0:
        data.remove(item)

print(data)
