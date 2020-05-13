import csv

FILENAME = "dataMax.csv"


def convert_base(num, to_base, from_base):
    if isinstance(num, str):  # проверяет принадлежность типу
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        first = convert_base(n // to_base, to_base,
                             from_base)  # делим до момента, пока не дойдем до цифр, входящих в данную СС
        second = alphabet[n % to_base]  # находим остаток
        num = first + second  # сложение строк
        return num

list_four = []
listCycle = []


def Kaprekar(num, digits, toRadix, fromRadix):
    count_cycle = 0
    used = []
    num = convert_base(num, toRadix, fromRadix)
    magic1 = num
    num = str(num)
    if len(num) < digits:
        num = num.zfill(digits)
    while True:
        if len(num) > digits:
            break
        magic = int(magic1)
        used.append(int(magic1))
        min = ''.join(map(str, sorted(num)))
        max = int(''.join(reversed(min)))
        min = int(min, toRadix)
        max = int(str(max), toRadix)
        num = int(max) - int(min)
        num = convert_base(num, toRadix, fromRadix)
        count_cycle = count_cycle + 1
        magic1 = int(num)
        if magic == magic1 and magic1 not in used[0:-1]:
            listCycle.append(count_cycle)
            return magic1
        elif magic == magic1 and count_cycle == 1:
            listCycle.append(count_cycle)
            return magic1
        elif magic1 in used[0:-1]:
            break

def f(list):
    n = []
    for i in list:
        if i not in n:
            n.append(i)
    return n

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    file.write("digit/radix/max_cycle/magic numbers\n")
    for radix in range(2, 11):
        t = 5453
        for digits in range(1, 7):
            nummm = ""
            num_before = []
            for number in range(1, 10 ** digits):
                length = len(str(number))
                if length > digits:
                    break
                num = Kaprekar(number, digits, radix, 10)
                if num != None and num not in num_before:
                    nummm = nummm + str(num) + " "
                    num_before.append(num)
            num_before.clear()
            list_four.append(str(digits) + " " + str(radix) + " " + nummm)
    list_len = len(list_four)
    listCycle.clear()
    Cycles = []
    for j in range(0, list_len):
        for number in range(1, 10000000):
            length = len(str(number))
            if list_four[j][3] == '0':
                radix = 10
            else:
                radix = int(list_four[j][2])
            digits = int(list_four[j][0])
            if length > digits:
                break
            num = Kaprekar(number, digits, radix, 10)
        listCycle.sort()
        listCycle.reverse()
        maximum = listCycle[0]
        new_str = ""
        start = 3
        if list_four[j][3] != " ":
            start = 4
        for k in range(start, len(list_four[j])):
            new_str = new_str + (str(list_four[j][k]))
        Cycles.append(str(list_four[j][0]) + str(list_four[j][1]) + str(radix) + "  " + str(maximum) + " " + new_str)
        listCycle.clear()
    dataN = []
    data = []
    for j in range(0, len(Cycles)):
        dataN.append([int(x) for x in Cycles[j].split()])
    for j in range(0, len(dataN)):
        file.write(str(dataN[j][0]) + " ")
        file.write(str(dataN[j][1]) + " ")
        file.write(str(dataN[j][2]) + " " + ": ")
        str_magic = ""
        for i in range(3, len(dataN[j]) - 1):
            str_magic += str(dataN[j][i]) +", "
        str_magic += str(dataN[j][len(dataN[j]) - 1])
        file.write(str_magic + "\n")
file.closed


