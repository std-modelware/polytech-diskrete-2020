def kaprekar(i, d, r):
    """
    Функция, осуществляющая один шаг алгоритма поиска постоянных Капрекара
    :param i: Число в дясятичной записи
    :param d: Число цифр числа(с учётом ведущих нулей)
    :param r: Система счиления
    :return: Результат одного шага
    """
    i = list_from_num(i, d, r)

    i.sort()
    major = list_to_num(i, r, d)

    i.reverse()
    minor = list_to_num(i, r, d)
    return major - minor


def max_num(d, r):
    '''
    Максимальное число из d цифр в r-чной системе счисления
    '''
    num = list()
    for i in range(d):
        num.append(r - 1)
    return list_to_num(num, r, d)


def list_to_num(dig_list, r, d):
    res = 0
    for i in range(len(dig_list)):
        res += dig_list[i] * r ** i
    return res


def list_from_num(i, d, r):
    dig_list = list()
    num = i
    for m in range(d):
        num, tmp = divmod(num, r)
        dig_list.append(tmp)
    return dig_list


def convert_base(i, to_base=10, from_base=10):
    """
    Смена системы счисления
    :param i: число
    :param to_base: в какую систему счисления перевести
    :param from_base: изначальная система счисления
    :return: число в новой системе счисления
    """
    num = str(i)
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def cycle_info(r, d):
    '''
    Функция, проводящая анализ всего множества чисел с указанными d и r
    :param r: Система счисления
    :param d: Число цифр
    :return: Список всех постоянных Капрекара, максимальная высота алгоритма до вхождения в цикл, максимальная длина цикла
    '''
    list_of_num = list()  # Проверенные числа
    all_cycles = list()  # Список циклов
    all_const = list()  # Список циклов длины 1(постоянные Капрекара)
    max_i = max_num(d, r)
    max_h = 0  # Максимальная глубина
    max_l = 0  # Максимальная длина цикла

    for i in range(max_i + 1):
        height = 0  # Глубина для данного числа
        list_of_res = list()  # Список результатов для данного числа

        '''
        Обоснование бесконечного цикла:
        Цикл точно существует, так как функция определна НА множестве чисел с параметрами r и d
        Функция никогда не выйдет за границы рамок r и d, тогда в худшем случае, рано или поздно произойдёт возврат к 
        начальному числу i, которое будет в списке, значит это так же цикл. Иначе будет найден другой цикл
        Исключение: 1...0, но оно корректно обрабатывается и возвращает нулевую константу на второй итерации 
        1000 - 0001 = 999(d уменьшилось) -> 999 - 999 = 0
        '''
        while True:
            height += 1
            res = kaprekar(i, d, r)  # Результат функции Капрекара для текущего числа

            try:  # Если полученное res уже есть в списке РЕЗУЛЬТАТОВ, значит цикл найден
                index = list_of_res.index(res)  # Индекс начала цикла

                if len(list_of_res[index::1]) == 1:  # Цикл длины один - это константа
                    all_const.append(list_of_res[index])

                if list_of_res[index:: 1] in all_cycles:  # Цикл уже был найден
                    break
                else:  # Добавляем новый цикл и обновляем информацию по max_l и max_h
                    all_cycles.append(list_of_res[index:: 1])
                    max_l = max(len(list_of_res[index:: 1]), max_l)
                    max_h = max(height, max_h)
            except ValueError:  # Если поймана ошибка, значит res нет в списке результатов -> добавляем
                list_of_res.append(res)

            if res in list_of_num:  # Если res уже в списке проверенных чисел, значит нет смысла проверять ещё раз
                break
            else:  # Иначе добавляем res в список проверенных чисел, так как дальше ТОЧНО будет проверка данного числа
                list_of_num.append(res)
            i = res  # Переход к следующей итерации
    return all_const, max_l, max_h


def research(file):
    '''
    Проведение исследования и запись результатов в указанный файл
    !!!Константы записываются в десятичной системе счисления!!!
    '''
    for r in range(2, 11):
        for d in range(1, 7):
            const, l, h = cycle_info(r, d)
            file.write("r = " + str(r) + " d = " + str(d) + "\n" + "Const list: ")
            for i in const:
                file.write(str(i) + " ")
            file.write("\nMax cycle length = " + str(l) + " Max height = " + str(h) + "\n\n")


f = open("research.txt", "w")
research(f)
f.close()
