import itertools

#String to list
def ToList(s: str):
    l = list()
    for i in range(0, len(s)):
        l += s[i]
    return l

#List to string
def ToStr(l: list):
    s = ''.join(l)
    return s

#Функция удаляет числа, которые могут быть получены циклическим сдвигом,
#нааходящиеся в изначальном списке l
def Cycle(l: list, n: int):
    res = list()
    count = 0
    for i in l:
        num = ToList(i)
        check = ToList(i)
        count = 0
        while int(count) < int(n-1):
            num.append(num.pop(0))
            if num == check:
                break
            if ToStr(num) in l:
                l.remove(ToStr(num))
            count += 1
    return l

#Циклический сдвиг числа на одну позицию вправо
def Shift(l: list):
        l.insert(0, l.pop())
        return l

#Различные комбинации числа длины n, полученного с использованием k единиц,
#без пвторений и чиел, которые могут быть получены циклическим сдвигом
def Combinations(n: int, k: int):
    tmp = list()
    l = list()
    l = '1'*k + '0'*(n-k)
    for i in itertools.permutations(l, n):
        n = ''.join(i)
        if n not in tmp:
            tmp.append(n)
    print(tmp)
    res = Cycle(tmp, int(n))
    return res

#Существует ли ось симметрии, проходящая от стороны многоугольника до его противоположной стороны
def Check(l: list):
    for i in range(0, len(l)//2):
        if l[i] != l[-1-i]:
            return False
    return True

#Существет ли ось симметрии, выходящая из одного угла многоугльника и приходящая в протиположный
def Check2(l: list):
    length = len(l)
    for i in range(1, length//2):
        if l[i] != l[length-i]:
            return False
    return True

#Поиск и вывод осей симметрии для одного числа
def Axis(num: list):
    l = len(num)
    if (l % 2) == 0:
        if Check(num) == True:
            print(num[0:len(num)//2], '  |  ', num[len(num)//2:]);
            return True
        elif Check2(num) == True:
            print('| ', num[0], ' | ', num[1:l//2], '| ', num[l//2], ' | ', num[l//2+1:l])
            return True
    else:
#Существует ли ось, выходящая из угла и приходящая на противолежащую сторону
        num = ToList(num)
        tmp1 = num.pop(0)
        #tmp2 = num.pop(l//2)
        if Check(num) == True:
            num.insert(0, int(tmp1))
            print('| ', num[0], ' | ', num[1:l])
            return True
    return False

#Основная функция для заданных n - количества цифр в числе и k - количества единиц находит все оси симметрии
#и их количество
def Symmetry(n: int, k: int):
    axis = 0
    count = 0
    l = list()
    l = Combinations(n, k)
    for num in l:
        print(num)
        axis = 0
        count = 0
        while int(count) < int(n):
            tmp = Axis(num)
            num = Shift(ToList(num))
            if tmp == True:
                axis += 1
            count += 1
        print('Number of axis: ', axis)


#MAIN
print('Put length of number:')
n = int(input())
print('Put number of ones:')
k = int(input())
Symmetry(n, k)
