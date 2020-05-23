
# Функция перевода числа в список цифр
# x - число
# s - система счисленя
# r - колличество разрядов в числе
def NumToList(x,s,r):
    res = list()
    num = x
    for i in range(r):
        data = num % s
        num = num // s
        res.append(data)
    res.reverse()
    return res

# Функция перевода списка цифр в число
# list - список
# s - система счисленя
# r - колличество разрядов в числе
def ListToNum(list,s,r):
    r1 = r - 1
    res = 0
    for i in range(r):
        res = res + list[i] * s ** r1
        r1 = r1 - 1
    return res

#Перевод числа из одной системы счисления в другую
# num - число
# SecondSystem -  вторая система счисленя
# FirstSystem - первая система счисленя
def ChangeSystemOfNumber(num, SecondSystem=10, FirstSystem=10):
    if isinstance(num, str):
        n = int(num, FirstSystem)
    else:
        n = int(num)
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < SecondSystem:
        return alph[n]
    else:
        return ChangeSystemOfNumber(n // SecondSystem, SecondSystem) + alph[n % SecondSystem]

#Шаг Капрекара
# num - число
# s - система счисленя
# r - колличество разрядов в числе
def Func(num, s, r):
    numerals = NumToList(num, s, r)
    numerals.sort()
    # минимальное число
    min =ListToNum(numerals, s,r)
    numerals.sort(reverse = True)
    # максимальное число
    max = ListToNum(numerals, s,r)
    return max - min

#Поиск чисел капрекара и длины цикла
# s - система счисленя
# r - колличество разрядов в числе
def Kap(s, r):
    data = 0
    Permanent = list()
    ListOfNums = list()
    n = 10 ** r
    length = 0
    size = 0
    for i in range(n):
        while(True):
            data = Func(i, s, r)
            if data == i:
                if data in Permanent:
                    break
                Permanent.append(data)
                break
            elif data in ListOfNums:
                break
            ListOfNums.append(data)
            i = data
            length = length + 1
        size = max(size, length)
        length = 0
    return Permanent, size
# открытие файла и последующая запись в него результата исследования
file = open("Kaprekar.txt", "w")
for s in range(2, 11):
     for r in range(2, 7):
        Permanent, size = Kap(s, r)
        for i in range(len(Permanent)):
            Permanent[i] = ChangeSystemOfNumber(Permanent[i], s, 10)
        file.write("система счисленя: " + str(s) + " колличество разрядов в числе: " + str(r) + " постоянные Капрекара: " + str(Permanent) +"\n длина цикла: " + str(size) + "\n")


file.close
