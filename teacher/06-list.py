# Список

# Списки могут содержать элементы РАЗНЫХ типов
# Список - изменяемый тип (добавление, изменение, удаления сожержимого НЕ ПРИВОДИТ к созданию нового объекта)

# Создание
list1 = list()
list2 = []

# Инициализация
list3 = [1, 2, 3, 4]

list4 = list('List')
print(list4)

# добавление
print(list3)
list3.append(5)
print(list3)

# доступ по индексу
print(list3[0], list4[3])

print(list3[-1], list3[len(list3) - 1])

# вставку
print(list3)
list3.insert(0, -1)
print(list3)

# обновление
list3[0] = 'test'
print(list3)

# удаление
list3.remove(3)
print(list3)
del list3[0]
print(list3)

# сортировка
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

list3_ = sorted(list3)
print('list3_ = ', list3_)

# сортировка по правилам (функция)
list3.append('aaa')
list3.append('zzz')
print(list3)
list3.sort(key=str)
print(list3)
list3.sort(key=str, reverse=True)
print(list3)

# range - полуинтервал
nums = range(5)
print(nums)
print(list(nums))

nums = range(10, 20, 2)
print(list(nums))

a = range(0, 5)
b = range(5, 10)
print(list(a) + list(b))

a = list(range(0, 10)) + list(range(0, 10)) + list(range(0, 5))
print(a)

import collections
print(collections.Counter(a))


