#r - система счисления, k - количество разрядов в числе

#Число -> список цифр
def ToList(num: int, k: int, r: int):
    digList = list()
    n = num
    for i in range(k):
        n, temp = divmod(n, r)
        digList.append(temp)
    return digList

#Список цифр -> число
def ToNum(l: list, k: int, r: int):
    n = 0
    for i in range(len(l)):
        n = n*r+l[i]
    return n
#Функция Капрекара, выполняющая один шаг
def Kaprekar(num: int, k:int, r:int):
    digList = ToList(num, k, r)
    digList.sort()
    min = ToNum(digList, k, r)
    digList.sort(reverse=True)
    max = ToNum(digList, k, r)
    return max - min

#Перевод числа из произвольной системы счисления в другую произвольную систему счисления
def Convert(num, to=10, fr=10):
    if isinstance(num, str):
        n = int(num, fr)
    else:
        n = int(num)
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to:
        return alph[n]
    else:
        return Convert(n // to, to) + alph[n % to]

#Функция вычисляет числа Капрекара и максимальный цикл
def SearchNumberAndCycles(k: int, r: int):
    new = 0
    length = 0
    maxLength = 0
    kapNums = list()
    nums = list()
    n = '9'*k
    for i in range(int(n)+1):
        while True:
            new = Kaprekar(i, k, r)
            if new == i:
                if new in kapNums:
                    break
                kapNums.append(new)
                break
            elif new in nums:
                break
            i = new
            nums.append(new)
            length += 1
        maxLength = max(maxLength, length)
        length = 0

    return kapNums, maxLength

#Для чисел в 2-6 системах счисления и разрядностью от 2 до 10 вычисляются числа Капрекара и максимальная длина цикла
def Research(file):
    for r in range(2, 11):
        for k in range(2, 7):
            nums, length = SearchNumberAndCycles(k, r)
            for i in range(len(nums)):
                nums[i] = Convert(nums[i], r, 10)
            file.write("Система счисления: " + str(r) + " Количество разрядов: " + str(k) + " Постоянные Капрекара: " + str(nums) +"\nМаксимальная длина цикла: " + str(length) + "\n")

#Исследование
fp = open("researchKaprekar.txt", "w")
Research(fp)
fp.close