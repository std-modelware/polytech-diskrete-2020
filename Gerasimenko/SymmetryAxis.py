import numpy
import matplotlib.pyplot as plot
import itertools


def ToString(num):
    STR = ""
    for i in num:
        STR += str(i)
    return STR

def BuiltNumbers(n, k):
    tmp = []
    #combinations генерирует уникальные числа = позиции единиц в двоичном числе
    for bits in itertools.combinations(range(n), k):
        s = [0] * n
        for bit in bits:
            s[bit] = 1
        tmp.append(s)

    #Функция, отсеивающая числа, которые могут быть получены циклическим сдвигом
    result = CyclesNumbers(tmp, n)
    return result

#Функция, отсеивающая числа, которые могут быть получены циклическим сдвигом
def CyclesNumbers(num, n):
    result = set()
    for j in range(num.__len__()):
        check = 0
        for i in range(n):
            num[j].insert(0, num[j].pop())
            if(ToString((num[j])) in result):
                check = 1
        if (check == 0):
            result.add(ToString((num[j])))
    return result

#По заданому значению i (порядковый номер вершины многоугольника с n вершинами) нахожу координаты
#соответсвующей вершины
def GetCoord(n, i, Radius):
    x = (Radius * numpy.cos(2 * numpy.pi * i / n))
    y = (Radius * numpy.sin(2 * numpy.pi * i / n))
    return x, y

#Данная функция принмает массивы, элементами которых являются массивы, состоящие из двух чисел
#Назову массивы, состоящие из двух чисел, например, подмассивами
#в случае массива Trough_numbers: два числа в подмассивах обозначают порядковый номер вершин, через которые проходит ось симм.
#в сулчае Between_numbers: если в подмассиве хранятся числа [n, m], значит, что ось симметрии проходит через две точки:
#первая точка находится между n и (n+1) вершинами, вторая точка между m и (m+1) вершинами
#в случае Mixed_numbers: если в подмассиве хранятся числа [n, m], значит, что ось симметрии проходит через две точки:
#первая точка это n-ая вершина, вторая точка находится между m и (m+1) вершинами
def Print(n, num, Trough_numbers, Between_numbers, Mixed_numbers):
    x = []
    y = []
    Radius = 2
    for i in range(n+1):
        x.append(Radius * numpy.cos(2 * numpy.pi * i / n))
        y.append(Radius * numpy.sin(2 * numpy.pi * i / n))
    plot.scatter(x, y, edgecolors='b', c='w')
    plot.plot(x, y)
    plot.title(num)
    #Подпись вершин
    for i in range(n):
        plot.text(x[i], y[i], str(num[i]))

    #Рисую линии симметрии, проходящие через числа
    for i in range(Trough_numbers.__len__()):
        x_tmp1, y_tmp1 = GetCoord(n, Trough_numbers[i][0], Radius)
        x_tmp2, y_tmp2 = GetCoord(n, Trough_numbers[i][1], Radius)
        plot.plot([x_tmp1, x_tmp2], [y_tmp1, y_tmp2])

    #Рисую линии симметрии, проходящие между числами
    for i in range(Between_numbers.__len__()):
        x_between = []
        y_between = []
        for j in range(0, 2):
            x_tmp1, y_tmp1 = GetCoord(n, Between_numbers[i][j], Radius)
            x_tmp2, y_tmp2 = GetCoord(n, Between_numbers[i][j] + 1, Radius)
            x_between.append( (x_tmp1 + x_tmp2) / 2 )
            y_between.append( (y_tmp1 + y_tmp2) / 2 )

        plot.scatter(x_between, y_between, edgecolors='r', c='w')
        plot.plot(x_between, y_between)

    #Рисую линии симметрии, проходящие через число и между числами одновременно
    for i in range(Mixed_numbers.__len__()):
        x_tmp1, y_tmp1 = GetCoord(n, Mixed_numbers[i][1], Radius)
        x_tmp2, y_tmp2 = GetCoord(n, Mixed_numbers[i][1] + 1, Radius)
        x_between = ((x_tmp1 + x_tmp2) / 2)
        y_between = ((y_tmp1 + y_tmp2) / 2)

        plot.scatter(x_between, y_between, edgecolors='r', c='w')
        plot.plot([x[Mixed_numbers[i][0]], x_between], [y[Mixed_numbers[i][0]], y_between])

    plot.show()

    
def Write(F, ele, Through_numbers, Between_numbers, Mixed_numbers):
F.write(str(ele) + "\n")
F.write("Through_numbers:\n")
for i in Through_numbers:
    F.write(str(i) + "\n")
F.write("Between_number:\n")
for i in Between_numbers:
    F.write(str(i) + "\n")
F.write("Mixed_numbers:\n")
for i in Mixed_numbers:
    F.write(str(i) + "\n")
F.write("\n\n")


def WriteDescription(F):
F.write("Through_number обозначает оси симметрии, проходящие через цифры = вершины многоугольника.\n"
        "В квадратных скобках числа в квадратных скобках обозначают номер цифр, через которые проходит ось\n"
        "Between_numbers обозначает сои симметрии, проходящие между цифрами.\n"
        "Допустим в квадратных скобках [n, m], значит, что ось симметрии проходит между"
        "n и (n+1) цифрами и между m и (m+1) цифрами\n"
        "Mixed_numbers обозначает оси симметрии, проходящие через цифру и между одновременно(в случае нечетного n)\n"
        "Допусти в квадратных скобках [n, m], значит, что ось симметрии проходит"
        "через n-ую цифру и между m и (m+1) цифрами\n\n\n")


#Рассмотрим случай, когда ось симметрии проходит через два числа
def AxisThroughNumbers(n, num):
    result = []
    for k in range(0, n//2):
        check = 0
        for i in range(1, n//2):
            t2 = k - i
            if(k + i >= n):
                t1 = abs(n - (k + i))
            else:
                t1 = k + i

            if(num[t1] != num[t2]):
                check = 1
                break
        if (check == 0):
            result.append([k, k + n // 2])
    return result

#Рассмотрим случай, когда ось симметрии проходит между числами
def AxisBetweenNumbers(n, num):
    result = []
    for k in range(0, n//2):
        check = 0
        for i in range(1, n//2 + 1):
            t2 = k - i + 1
            if (k + i >= n):
                t1 = abs(n - (k + i))
            else:
                t1 = k + i

            if (num[t1] != num[t2]):
                check = 1
                break
        if (check == 0):
            result.append([k, k + n // 2])
    return result

#Рассмотрим случай, когда ось симметрии проходит через число и между числами одновременно
def AxisMixedNumbers(n, num):
    result = []
    for k in range(0, n):
        check = 0
        for i in range(1, n//2 + 1):
            t2 = k - i
            if (k + i >= n):
                t1 = abs(n - (k + i))
            else:
                t1 = k + i

            if (num[t1] != num[t2]):
                check = 1
                break
        if (check == 0):
            result.append([k, k + n // 2])
    return result

def SymmetryAxis(result, n):
    count = 0
    for ele in result:
        Through_numbers = []
        Between_numbers = []
        Mixed_numbers = []
        num = list(ele)
        if(n % 2 == 0):
            #Рассмотрим случай, когда ось симметрии проходит через два числа
            Through_numbers = AxisThroughNumbers(n, num)
            count += Through_numbers.__len__()

            #Рассмотрим случай, когда ось симметрии проходит между числами
            Between_numbers = AxisBetweenNumbers(n, num)
            count += Between_numbers.__len__()
        if(n % 2 != 0):
            #Рассмотрим случай, когда ось симметрии проходит через число и между числами одновременно
            Mixed_numbers = AxisMixedNumbers(n, num)
            count += Mixed_numbers.__len__()

        Print(n, num, Through_numbers, Between_numbers, Mixed_numbers)
    print(count)

###  MAIN  ###
F = open('result.txt', 'w')
print("Input n:")
n = int(input());
print("Input k:")
k = int(input());
result = BuiltNumbers(n, k)
WriteDescription(F)
SymmetryAxis(result, n, F)
F.close()
