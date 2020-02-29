# Переменные
# Переменные указывают на объекты (экземпляры класса)
i = 1
print(type(i))

# print(dir(i))

i = 'one'
print(type(i))

print(id(i))

j = 'one'
print(id(j))

print(i is j)

a = [1, 2]
b = a
b = [1, 2]
print(a)
print(id(a))
print(id(b))

# Типы
i = 'str'
print(type(i))  # строка
i = 10
print(type(i))  # число
i = 10.0
print(type(i))  # действительное число
i = True
print(type(i))  # логическое выражение
i = [1, 2, 3, 4, 'www']
print(type(i))  # списков
i = {'one': 1}
print(type(i))  # словарь
i = {1, 2, 3, 4, 'www'}
print(type(i))  # множество
i = tuple([1])
print(type(i))  # кортеж

def func():
    return 1

print(type(func))

print('aaaaa'.capitalize())
print(type('aaaaa'.capitalize))

print(dir(func))
print(help(func))

print(type(None))

# Объекты делятся на две группы: неизменяемые и изменяемые
# Изменяемые: dict, list
# Неизменяемые: int, string, tuple

age = 18
print(id(age))
age = age + 1
print(id(age))

age = [18]
print(age)
print(id(age))
age.append(20)
print(age)
print(id(age))
