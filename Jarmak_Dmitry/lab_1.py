import sys


# Вспомогательные функции
# Перевод в заданную систему счисления
def convert(number, base=10):
    if base > 10:
        return 0
    chars = "0123456789"
    div, mod = divmod(number, base)
    if number < base:
        return chars[number]
    return convert(div, base=base) + chars[mod]


def align(number, size, n):
    while (size < n):
        number = '0' + number
        size += 1


#Заранее создаем массив с числами, которые подвергнем анализу на свойства Капрекара. Для этого отберем числа определенной
# разрядности и в определенной системе счисления такие, которые отсортированы
# по возрастанию (минимумы)
def create_required_num(number, digits, numbers, base=10):

    align(number, len(number), digits)

    data = [int(i, base=base) for i in number]

    data.sort()
    mins = 0
    for i in range(digits):
        mins += data[i]*base**i

    if mins not in numbers:
        numbers.append(convert(mins, base=base))


def find_out_kaprekar(a, b, digits, numbers, base=10):
    for i in range(a, b):
        create_required_num(convert(i, base=base), digits, numbers, base=base)


# Универсальная функция для работы с числами Капрекара (вычитания)
def kaprekar_for_fun(num, count, base=10):

    align(num, len(num), count)

    digits = [int(i, base=base) for i in num]

    digits.sort()
    mins = 0
    for i in range(count):
        mins += digits[i]*base**i

    digits.reverse()
    maxs = 0
    for i in range(count):
        maxs += digits[i]*base**i

    diff = abs(maxs - mins)

    return convert(diff, base=base)
#===================================================================================================================


# Универсальная функция для набора тестов (ищем неподвижную точку или цикл(ы))
def tests_for_kaprekar(number, digits, base, magicNumbers, magicCycles):
    iterator_count = 0
    previous = []
    flag = False

    while True:
        next_c = number
        previous.append(number)
        number = kaprekar_for_fun(number, digits, base=base)

        while len(number) < digits:
            number = '0' + number

        if int(number, base) == 0:
            break
        #нашли неподвижную точку, если ее нет, то добавляем в массив, иначе смотрим максимальную глубину древа
        #(количество итераций, необходимых для обнаружения числа)
        if next_c == number:
            if magicNumbers.get(number) == None:
                magicNumbers[number] = (base, digits, iterator_count)
            elif magicNumbers[number][2] < iterator_count:
                magicNumbers[number] = (base, digits, iterator_count)
            break
        #Проверяем на цикл
        else:
            if number in previous:
                while previous[0] != number:
                    del previous[0]
                # Проверяем наличие числа в цикле
                for mass in magicCycles:
                    if flag == True:
                        break
                    if mass[1] == base:
                        for number_c in mass[0]:
                            if number_c == previous[0]:
                                flag = True
                                break
                if flag == False:
                    #Записываем цикл, систему счисления, количество цифр, длину цикла
                    magicCycles.append((previous[:], base, digits, len(previous)))
                break
        flag = False
        iterator_count += 1


def printTable(magicNumbers, cycle_info, base_max, digits_max):

    #Создаем двумерный массив для таблицы
    # 1- есть или нет неподвижной точки (если имеются, то выводим их в таблицу, иначе NONE)
    # 2- максимальная глубина древа
    # 3- Количество циклов
    # 4- длина наибольшего цикла

    table = [[0] * (base_max - 1) for i in range(digits_max - 1)]

    for key, val in magicNumbers.items():
        # - 2, чтобы иметь нумерацию с нуля
        if table[len(key) - 2][val[0] - 2] == 0:
            table[len(key) - 2][val[0] - 2] = [key, val[2], 0, 0]
        else:
            table[len(key) - 2][val[0] - 2][0] += " " + key
            if table[len(key) - 2][val[0] - 2][1] < val[2]:
                table[len(key) - 2][val[0] - 2][1] = val[2]

    for items in cycle_info:
        #Нашли первый цикл, постоянная Капрекара - отсутсвует
        if table[len(items[0][0]) - 2][items[1] - 2] == 0:
            table[len(items[0][0]) - 2][items[1] - 2] = ["NONE", 0, 1, items[3]]
        elif table[len(items[0][0]) - 2][items[1] - 2][2] == 0 \
                and table[len(items[0][0]) - 2][items[1] - 2][0] != "NONE":
            #Есть как число Капрекара, так и цикл
            table[len(items[0][0]) - 2][items[1] - 2][2] += 1
            table[len(items[0][0]) - 2][items[1] - 2][3] = items[3]
        else:
            #Нашли еще цикл - смотрим длину
            table[len(items[0][0]) - 2][items[1] - 2][2] += 1
            if table[len(items[0][0]) - 2][items[1] - 2][3] < items[3]:
                table[len(items[0][0]) - 2][items[1] - 2][3] = items[3]
                
    #построениe таблицы
    k = [str(i) + " base" for i in range(2, base_max + 1)]
    print("          ", end='')
    for i in k:
        print("                        " + i, end="")
    print()

    for i in range(0, digits_max - 1):
        print("digits {:d}:".format(i + 2), end=" ")
        for j in range(0, base_max - 1):
            if len(str(table[i][j])) < 30:
                for k in range(len(str(table[i][j])), 30):
                    print(end=" ")
            print(table[i][j], end="")
        print()
    return 0


def main():
    magicNumbers = {}
    cycle_info = []
    suspicious_numbers = []
    radix = 2
    base_max = 10
    digits_max = 4 #Для 6 вычисления получаются достаточно долгими
    number = int(input("Please, input something to start the program: "))

    while radix < base_max + 1:
        for j in range(2, digits_max + 1):
            find_out_kaprekar(radix**(j - 1), radix**j - 1, j, suspicious_numbers, radix)
            for number in suspicious_numbers:
                tests_for_kaprekar(number, j, radix, magicNumbers, cycle_info)
            suspicious_numbers.clear()
        radix += 1

    #Выводим неподвижные точки, циклы, таблицу
    print("Kaprekar numbers!: ", magicNumbers)
    print("Cycles!: ", cycle_info)
    printTable(magicNumbers, cycle_info, base_max, digits_max)


if __name__ == "__main__":
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main()
