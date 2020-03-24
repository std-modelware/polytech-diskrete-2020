# Преобразование числа в список
def num2arr(num):
    arr = []
    while num != 0:
        arr.append(num % 10)
        num = num // 10
    arr.reverse()
    return arr

# Преобразование списка в число
def arr2num(number_list):
    res = 0
    deg = len(number_list) - 1
    for numeral in number_list:
        res += numeral * (10 ** deg)
        deg -= 1
    return res

# Проверка, является ли данное число Капрекаровым
def kaprekar(number_list, base):
    num = arr2num(number_list)
    number_list.sort(reverse=True)
    num1 = number_list
    num2 = []
    num2.extend(num1)
    num2.reverse()
    if base_residual(num1, num2, base) == num:
        return 1
    else:
        return 0

# Разность с учётом системы счисления (ВАЖНО - num1 по умолчанию меньше num2)
def base_residual(num1, num2, base):
    i = len(num1) - 1
    if i == 0:
        return num1[i] - num2[i]
    ans = []
    while i >= 0:
        if num1[i] < num2[i]:
            tmp_res = num1[i] + base - num2[i]
            num1[i - 1] -= 1
        else:
            tmp_res = num1[i] - num2[i]
        ans.append(tmp_res)
        i -= 1
    ans.reverse()
    ans = arr2num(ans)
    return ans

# Перевод числа из десятичной системы счисления в произвольную
def dec2base(dec, base):
    if base == 10:
        return dec
    num = []
    while dec > 0:
        num.append(dec % base)
        dec //= base
    num.reverse()
    num = arr2num(num)
    return num

# Погнали
def run():
    base_list = list(range(2, 11))
    output_list = []
    for base in base_list:
        print('Система счисления:', base)
        number = 0
        prev_len = 1  # Чтобы не выводить ноль
        flag = 0
        while True:
            tmp_number = dec2base(number, base)
            number_list = num2arr(tmp_number)
            tmp_len = len(number_list)
            if tmp_len != prev_len and output_list != []:
                print('   Количество цифр:', prev_len)
                print('    ', output_list)
                output_list = []
            if tmp_len > 6:
                if flag == 0:
                    print('     Числа Капрекара отсутствуют')
                break
            if kaprekar(number_list, base) == 1:
                if prev_len == tmp_len:
                    output_list.append(tmp_number)
                    flag = 1
            number += 1
            prev_len = tmp_len


run()
