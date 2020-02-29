# Логический тип

print(True)
print(False)

print(bool(1))
print(bool(0))
print(bool(100))

print(bool(1.0))
print(bool(0.0))
print(bool(100.0))

print(bool([]))
print(bool([1, 2]))

if []:
    print('1:error')
else:
    print('1:empty')

if bool([]):
    print('2:error')
else:
    print('2:empty')

if [1, 2]:
    print('3:not empty')
else:
    print('3:error')

if bool([1, 2]):
    print('4:not empty')
else:
    print('4:error')

print(bool({}))
print(bool({'s': 's'}))

print(bool('sssss'))
print(bool(''))

i = 10
print(bool(i))
i = None
print(bool(i))


def func():
    i = 10


print(func())

# None
a = None
print(id(a))

b = None
print(id(b))

print(a is b)
print(a is not b)
