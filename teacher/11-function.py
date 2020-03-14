# Функции
# Все инструкции выполняются последовательно, поэтому функции должны быть определены ДО их первого использования

def plus_2(num):
    '''
    Возвращает увеличенное на 2 входное значение
    :param num:
    :return:
    '''
    return num + 2


print(type(plus_2))

help(plus_2)

res = plus_2(10)
print(res)

# Области видимости переменных
g = 10


def scope():
    # global g
    l = 23
    g = 100
    print(l)
    print(g)
    print(globals())  # список глобальных переменных
    print(locals())  # список локальных переменных


print(g)
scope()
print(g)


def summary(a, b):
    return a + b


print(summary(1, 2))
print(summary("1", "2"))


# print(summary("1", 2))

# параметры по умолчанию
# В качестве параметров по умолчанию НЕ рекомендуется использовать изменяемые типы
# Параметры по умалчанию создаются ОДИН раз при определении функции
# Если используется ИЗМЕНЯЕМОЕ значение, то при каждом вызове функции будет использован ОДИН и ТОТ ЖЕ экземпляр
def summary2(a, b=2):
    return a + b * 2


print(summary2(10, 20))
print(summary2(20, 10))
# можно сопоставлять параметры по ключам
print(summary2(b=20, a=10))

f = summary
print(f(1, 2))


def callback(f, a, b):
    return f(a, b)


print(callback(summary, 1, 2))
print(callback(f, 1, 2))

# def присваивает ссылку на объект-функцию идентификатору, который стоить после def
n = 10
if n == 1:
    def f1():
        print('f1')
else:
    def f1():
        print('f1 new')

f1()


def f1():
    print('f1 new new')


f1()

# анонимные функции
af = lambda x, y: x + y
print(af(12, 13))


# функции-генераторы
# функции при последовательных вызовов которых возвращается очередной элемент какой-либо последовательности
def genfunc(count):
    for i in range(0, count + 1):
        yield i

for i in genfunc(5):
    print(i)

print(genfunc(6))
print(genfunc(6).__next__())

# функции-декораторы
# позволяют выполнять действие ПЕРЕД выполнением функции
# в качестве параметры используется ссылка на функцию, а возвращаемое значение тоже ссылка на функцию

def do_nothing():
    return None

def deco(f):
    print('call f')
    # return f
    return do_nothing

@deco
def empty(x):
    return x

print('-' * 10)
print (empty(10))