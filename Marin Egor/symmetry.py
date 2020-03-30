import itertools


def even(n: int):
    return n % 2 == 0


def axis_points(n: int, k: int):
    '''
    Возвращает возможные оси симметрии для данных n и k
    '''
    if even(n) and even(k):
        return ['00', '11', '']
    elif not even(n) and even(k):
        return ['0']
    elif even(n) and not even(k):
        return ['10']
    else:
        return ['1']


def all_combinations(n: int, k: int):
    '''
    Все возможные многоугольники для данных n и k, с учётом эквивалентных по циклическому сдвигу
    Это нужно для последующей проверки числа на наличие оси симметри в функции check за O(n/2)
    '''
    a = '1' * k + '0' * (n - k)
    for i in itertools.product('10', repeat=n):
        if i.count('1') == k:
            yield list(i)
    return


def check(num: list, n: int, cut: str):
    '''
    Проверяет, есть ли данная ось симметрии в многоугольнике
    '''
    l = len(cut)
    if l == 0:
        i = n // 2
        j = n // 2 - 1
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    elif l == 1:
        if num[0] != cut[0]:
            return False
        i = (n - 1) // 2 + 1
        j = i - 1
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    else:
        if num[0] != cut[0] or num[n // 2] != cut[1]:
            return False
        i = n // 2 + 1
        j = i - 2
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    return True


def search_axis(i: list, cuts: list):
    axis_list = []
    # Для каждой возможной оси симметрии
    for cut in cuts:
        # Если ось найдена, добавляем в список
        if check(i, len(i), cut):
            axis_list.append([i, cut])
    return axis_list


def symmetry_polygons(n: int, k: int):
    '''
    Находит все классы эквивалентности для задачи нахождения оси симметрии бинарного многоугольника
    :param n: количество углов
    :param k: количество единиц
    :return: list(list(str(1|0)), str(axis))
    '''
    # Возможные оси для данных n и k
    points = axis_points(n, k)
    polygons = []
    # Для всех возможных многоугольников
    for i in all_combinations(n, k):
        #print(i, points)
        polygons += search_axis(i, points)  # Добавляем все оси симметрии для многоугольника
    return polygons


def draw_axis(polygons: list):
    for i in polygons:
        if len(i[1]) == 0:
            i[0].insert(len(i[0]) // 2, '|')
        else:
            i[0].insert(1, ']')
            i[0].insert(0, '[')
            if len(i[1]) == 2:
                i[0].insert(len(i[0]) // 2 + 1, '[')
                i[0].insert(len(i[0]) // 2 + 3, ']')


input_data = input().split()
p = symmetry_polygons(int(input_data[0]), int(input_data[1]))
draw_axis(p)
for i in p:
    res = ''
    for sym in i[0]:
        res += sym
    print(res)
