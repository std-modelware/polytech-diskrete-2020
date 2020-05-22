def StrToNum(str, syst): #перевод происходит в 10-ичную систему счисления
    result = 0
    str.reverse()
    for i in range(len(str)):
        result += str[i] * syst ** i
    return result

def NumToStr(num, syst, size): # перевод числа в строку (в нужной системе счисления)
    tmp = num
    result = []
    for i in range(size):
        tmp, ost = divmod(tmp, syst)
        result.append(ost)
    return result

def MainFunc(number, size, system): # основная формула, использованная в функции Капрекара
    numerals = NumToStr(number, system, size)
    numerals.sort()
    minuen = StrToNum(numerals, system) # минимальное число из данного набора цифр
    numerals.sort(reverse = True)
    subt = StrToNum(numerals, system) # максимальное число из данного набора цифр
    return subt - minuen # шаг функции Каперкара


def ConvToSystem(number, prev = 10, cur = 10): # перевод из одной выбранной системы счисления в другую
    res = 0
    if isinstance(number, str):
        tmp = int(number, prev)
    else:
        tmp = int(number)
    alp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (tmp < cur):
        return alp[tmp]
    else:
        res = ConvToSystem(tmp // cur, 10, cur)
        return res + alp[tmp % cur]


def ResearchUnit(system, size): # нахождение числа Капрекара для данной размерности чисел и систем счисления
    tmp = 0
    l = 0
    lMagic = 0
    const = list()
    exist_list = list()
    total = 10 ** size
    for i in range(total): # цикл по всем числам в данной размерности
        while(True):
            tmp = MainFunc(i, size, system) # отрабатываем функцие йКаперкара данное число
            if (tmp == i):
                if (tmp in const):
                    break
                const.append(tmp)
                break
            elif (tmp in exist_list):
                break
            exist_list.append(tmp)
            i = tmp # продолжаем работать с одним числом, пока не придем в стационарную "магическую точку"
            l += 1
        if (l >= lMagic):
            lMagic = l
        l = 0
    return const, lMagic

file = open("CaprekarNumbers.txt", "w") # текстовый документ под запись результатов

systemStart = 2
systemEnd = 10 # границы исследуемых систем счисления (здесь - нижняя, а строкой выше - верхняя)
numeralStart = 2
numeralEnd = 6 # границы размеров исследуемых чисел
file.write("Number size/ System/ Set of numbers/ Max iterations\n")
for syst in range(systemStart, systemEnd + 1):
    for size in range(numeralStart, numeralEnd + 1):
        const, lMax = ResearchUnit(syst, size)
        for i in range(len(const)):
            const[i] = ConvToSystem(const[i], 10, syst)
        #print("Radix: " + str(syst) + "\t" + "d: " + str(size) + "\t" + "List of nums: " + str(const) + "\n\t\t\t" + "Max length: " + str(lMax) + "\n")
        print("" + str(size) + ", " + "\t" + str(syst) + ", " + "\t" + str(const) + ", " + "\t" + "MaxIters = " + str(lMax) + "\n")
        file.write("" + str(size) + ", " + "\t" + str(syst) + ", " + "\t" + str(const) + ", " + "\t" + "MaxIters = " + str(lMax) + "\n")
file.close()




