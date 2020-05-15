def ConvToDec(number: str, r: int):  # Перевод в десятичную систему счисления
    return int(number, r)


def ConvFromDec(number: int, r: int):  # Перевод из десятичной системы счисления в другую систему счисления
    alphabet = ('A', 'B', 'C', 'D', 'E', 'F')
    res = []

    if number == 0:
        return '0'

    i = 0
    while number > 0:
        temp = number % r
        res.append(temp)
        number = number // r
        if res[i] >= 10:
            j = 0
            while res[i] != j + 10:
                j += 1
            res[i] = alphabet[j]
        i += 1

    res.reverse()
    res: str = "".join(map(str, res))
    return res


def FillNumber(number: str, d: int):  # Дополнение недостающих позиций нулями
    return '0' * (d - len(number)) + number


def Kaprekar(number: str, r: int):  # Метод Капрекара
    number_list = list(number)
    min_number = int(''.join(sorted(number_list)), r)
    max_number = int(''.join(sorted(number_list, reverse=True)), r)
    return max_number - min_number


def FindMagicNumber(number: str, r: int, d: int):  # Поиск магического числа и подсчет количества итераций
    iteration = 1
    while number != FillNumber(ConvFromDec(Kaprekar(number, r), r), d):
        iteration += 1
        number = FillNumber(ConvFromDec(Kaprekar(number, r), r), d)
        if iteration > 10:
            break
    return iteration, number


magic_numbers = []
MAX_LENGTH = 6
MAX_SYSTEM = 16

file = open("results.txt", "w")

for r in range(2, MAX_SYSTEM + 1):
    for d in range(2, MAX_LENGTH + 1):
        file.write("System: {0}\tlength: {1}\n".format(r, d))
        print("System: {0}\tlength: {1}\n".format(r, d))
        for number in range(r ** d):
            number = ConvFromDec(number, r)
            number = FillNumber(number, d)
            iteration, magic_number = FindMagicNumber(number, r, d)
            if iteration != 0 and (magic_number, r) not in magic_numbers:
                magic_numbers.append((magic_number, r))
                file.write("'{0}': {1}; ".format(magic_number, iteration))
        file.write("\n")

file.close()
