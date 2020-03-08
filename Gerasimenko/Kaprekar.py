#перевод систем счисления
def convert_base(num, to_base, from_base = 10):
    n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

# Функция, создающая массив цифр числа
def NumbersMass(number_str, number_count, base):
    number_str = number_str.rjust(number_count, '0')
    num_str = [int(ch, base) for ch in number_str]
    return num_str

#Функция Капрекара(вычитаем из максимального числа минимальное)
def Kaprekar(num, number_count, base):
    number_str = str(num)
    num_str = NumbersMass(number_str, number_count, base)
    num_str.sort()
    min_num = sum(digit * base ** i for i, digit in enumerate(num_str[::-1]))
    num_str.reverse()
    max_num = sum(digit * base ** i for i, digit in enumerate(num_str[::-1]))
    res = convert_base(max_num - min_num, base)
    res = res.rjust(number_count, '0')
    return res

#Функция для нахождения неподвижных точек Капрекара
def KaprekarNumbers(num, number_count, base):
    num_str = convert_base(num, base)
    num_str = num_str.rjust(number_count, '0')
    check = Kaprekar(num_str, number_count, base)
    #num_base = convert_base(num, base)
    if (num_str == check): 
        return True, num_str
    else:
        return False, num_str



# Функция, находящая неподвижные точки Капрекара, так же находящая количестов циклов и наибльшую длину цикла для каждой системы счисления
# и каждого разряда числа
def CyclesLength(max_number, number_count, base):
    length = 0
    loop_count = 0
    list_loop = []
    kaprekar_num = []
    for num in range(max_number):
        checkKaprekar = False
        checkKaprekar, num_str = KaprekarNumbers(num, number_count, base)
        if(checkKaprekar == True):
            kaprekar_num.append(num_str)
        cur_length = 0
        list_cycle = []
        num_str = convert_base(num, base)
        num_str = num_str.rjust(number_count, '0')
        list_cycle.append(num_str)
        last_num = Kaprekar(num_str, number_count, base)
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
            last_num = Kaprekar(last_num, number_count, base)
        if cur_length > length and loop_count != 0:
            length = cur_length
    return kaprekar_num, loop_count, length


# Данная функция 
# Вызывает основную функцию CyclesLength, которая находит неподвижные точки Капрекара, считает количество циклов и наибольшую длинну цикла
def BuiltTable():
    number_count = 5
    base = 10
    for i in range(2, base+1):
        for j in range(1, number_count+1):
            kaprekar_num, loop_count, length = CyclesLength(i**j, j, i)


#main
BuiltTable()






