#перевод систем счисления
def convertSystem(num, num_system, orig_num_base = 10):
    n = int(num)
    alphabet = "0123456789ABCDEF"
    if n < num_system:
        return alphabet[n]
    else:
        return convertSystem(n // num_system, num_system) + alphabet[n % num_system] #// - целочисленное деление

# Функция, создающая массив цифр числа
def numToArray(num, number_count, base):
    num = num.rjust(number_count, '0')
    num = [int(ch, base) for ch in num]
    return num

def KaprekarMove(num, number_count, base):
    number_str = str(num)
    num_arr = numToArray(number_str, number_count, base)
    num_arr.sort()
    min_num = sum(digit * base ** i for i, digit in enumerate(num_arr[::-1]))# ** - возведение в степень
    num_arr.reverse()
    max_num = sum(digit * base ** i for i, digit in enumerate(num_arr[::-1]))
    res = convertSystem(max_num - min_num, base)
    res = res.rjust(number_count, '0') #добавление слева нулей числу
    return res


def KaprekarNumbers(num, number_count, base):
    num_str = convertSystem(num, base)
    num_str = num_str.rjust(number_count, '0')
    check = KaprekarMove(num_str, number_count, base)
    if (num_str == check): #and num != 0:
        return True, num_str
    else:
        return False, num_str


def CyclesLength(max_number, number_count, base):
    length = 0
    loop_count = 0
    list_loop = []
    kaprekar_num = []
    checkKaprekar = False
    for num in range(max_number):
        checkKaprekar, num_str = KaprekarNumbers(num, number_count, base)
        if(checkKaprekar):
            kaprekar_num.append(num_str) # добавление в список числе Капрекара
        cur_length = 0
        list_cycle = []
        num_str = convertSystem(num, base)
        num_str = num_str.rjust(number_count, '0')
        list_cycle.append(num_str)
        last_num = KaprekarMove(num_str, number_count, base)
        while True:
            if(last_num in list_cycle):
                k = list_cycle.__len__() - 1
                check = 0
                while(list_cycle[k] != last_num and list_cycle[k] not in list_loop):
                    list_loop.append(list_cycle[k])
                    cur_length += 1
                    k -= 1
                    check = 1
                list_loop.append(list_cycle[k])
                cur_length += 1
                if (check == 1):
                    loop_count += 1
                break
            list_cycle.append(last_num)
            last_num = KaprekarMove(last_num, number_count, base)
        if cur_length > length and loop_count != 0:
            length = cur_length
    return kaprekar_num, loop_count, length


# Открытие и запись в таблицу
def WriteTable():
    import numpy as np
    import pandas as pd
    import time


    max_number_length = 6
    max_base = 16
    matrix = np.empty((max_base - 1, max_number_length), dtype ='U70') # U70 - null-terminated Unicode strings of max length 70
    for i in range(2, max_base + 1): # по системам счисления
        start_time_buf = time.time()
        for j in range(1, max_number_length + 1): # по длине числа
            num_count = i**j #base^max_number_length
            kaprekar_num, loop_count, length = CyclesLength(num_count, j, i)
            str_im = str(kaprekar_num) + '|' + str(loop_count) + '|' + str(length)
            matrix[i - 2][j - 1] = str_im
            print("system: %s   digits length::" % i, j)
        print("%s seconds for %s base" % (time.time() - start_time_buf, i))

    indexes = []
    for i in range(2, max_base+1):
        indexes.append('base ' + str(i))
    COLUMNS = []
    for i in range(1, max_number_length + 1):
        COLUMNS.append('numbers ' + str(i))
    table = pd.DataFrame(matrix, index = indexes, columns = COLUMNS)
    table.to_csv(r'D:\Python\Числа Капрекара.csv', index = True, header=True)

import time

start_time = time.time()

WriteTable()

print("final time:" % (time.time() - start_time))

