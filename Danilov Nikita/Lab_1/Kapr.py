# Cписок в число
def list2number(number_list):
    res = 0
    deg = len(number_list) - 1
    for numeral in number_list:
        res += numeral * (10 ** deg)
        deg -= 1
    return res

# Число в список
def number2list(number):
    number_list = []
    while number != 0:
        number_list.append(number % 10)
        number = number // 10
    number_list.reverse()
    return number_list

# Число из десятичной с.с. в произвольную
def decimal2base(dec, base, length):
    if dec == 0:
        return [0]
    num_list = []
    res = []
    while dec > 0:
        num_list.append(dec % base)
        dec //= base
    num_list.reverse()
    if len(num_list) < length:
        for i in list(range(0, length - len(num_list))):
            res.append(0)
        res.extend(num_list)
        return res
    return num_list

#Число из произвольной с.с. в десятичную
def base2decimal(number_list, base):
    num = 0
    deg = len(number_list) - 1
    for pos in number_list:
        num += pos * (base ** deg)
        deg -= 1
    return num

#Вычитание с учетом разряда и разрядности числа
def Subtraction(number, base, length):
    number_list = decimal2base(number, base, length)
    number_list.sort()
    little = base2decimal(number_list, base)
    number_list.reverse()
    big = base2decimal(number_list, base)
    # print(big - little)
    return decimal2base(big - little, base, length)

def Kaprekar():
    output_set = set()
    iter_limit = 1
    for base in list(range(2, 11)):
        print('Основание системы счисления: ', base)
        length = 2
        #print(' Количество цифр в числе: ', length)
        flag = 0
        for current in list(range(base, 1 + base ** 6)):
            num_list = decimal2base(current, base, length)
            if len(num_list) > length:  # Когда разрядность увеличивается на 1
                print('     Количество цифр в числе: ', length)
                if flag == 0:
                    print('         Постоянной капрекара (нетривиальной) для этого количества разрядов не существует!')
                    output_set.clear()
                else:
                    print('     ', output_set)
                    output_set.clear()
                    flag = 0
                length += 1
            iter = 0
            numer = current
            while True:
                numer_list = decimal2base(numer, base, length)
                iter += 1
                numer_list.sort()
                res = Subtraction(numer, base, length)
                res_list = res.copy()
                res_list.sort()
                if numer_list == res_list and res_list != {0}:
                    flag = 1
                    output_set.add((''.join([str(i) for i in res])))
                    break
                if iter > iter_limit or res == [0]:
                    break
                numer = base2decimal(res, base)

Kaprekar()