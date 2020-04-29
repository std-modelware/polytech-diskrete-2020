import numpy as np
import itertools as it


def sym_print(arr, sz, param):
    half = int(sz / 2)
    # Длина чётная
    if sz % 2 == 0:
        # Ось проходит через две противоположные вершины
        if param == 1:
            for i in range(1, half):
                print(arr[i], end=' ')
            print('(', arr[0], ' axis ', arr[half], ')', end=' ')
            for i in range(half + 1, sz):
                # print('!!!', i)
                print(arr[i], end=' ')
        # Ось проходит через два противоположных рёбра
        if param == 0:
            for i in range(0, half):
                print(arr[i], end=' ')
            print(' ( axis ) ', end=' ')
            for i in range(half, sz):
                print(arr[i], end=' ')
    # Длина нечётная
    else:
        # Ось проходит через вершину и противоположное ребро
        for i in range(1, half + 1):
            print(arr[i], end=' ')
        print('( ', arr[0], ' axis )', end=' ')
        for i in range(half + 1, sz):
            print(arr[i], end=' ')
    print('')


def shift(arr, sz):
    tmp = arr[0]
    for i in range(1, sz):
        arr[i - 1] = arr[i]
    arr[sz - 1] = tmp


def k_count(arr, sz):
    counter = 0
    for i in range(0, sz):
        if arr[i] == 1:
            counter += 1
    return counter


def comp(arr1, arr2, sz):
    for i in range(0, sz):
        if arr1[i] != arr2[i]:
            return 0
    return 1


def eq_check(arr1, arr2, sz):
    for i in range(0, sz):
        if comp(arr1, arr2, sz) == 1:
            return 1
        shift(arr2, sz)
    return 0


def sym_check(arr, sz):
    sym_counter = 0
    half = int(sz / 2)
    # Длина чётная
    if sz % 2 == 0:
        # Ось проходит через две противоположные вершины
        for j in range(0, half):
            flag = 0
            for i in range(1, half):
                if arr[i] != arr[sz - i]:
                    flag = 1
                    break
            if flag == 0:
                sym_counter += 1
                sym_print(arr, sz, 1)
            shift(arr, sz)
        # Ось проходит через два противоположных рёбра
        for j in range(0, half):
            flag = 0
            for i in range(0, half):
                if arr[i] != arr[sz - 1 - i]:
                    flag = 1
                    break
            if flag == 0:
                sym_print(arr, sz, 0)
                sym_counter += 1
            shift(arr, sz)
    # Длина нечётная
    else:
        # Ось проходит через вершину и противоположное ребро
        for j in range(0, sz):
            flag = 0
            for i in range(1, half + 1):
                if arr[i] != arr[sz - i]:
                    flag = 1
                    break
            if flag == 0:
                sym_print(arr, sz, 0)
                sym_counter += 1
            shift(arr, sz)
    if sym_counter > 0:
        print('Следующий класс эквивалентности')
    return sym_counter


def eq(n, k):
    eq_list = list()
    st = '0' * (n - k)
    st = st + '1' * k
    arr = np.array(list(st), int)
    eq_list.append(arr)
    eq_counter = 1
    for per in it.product('10', repeat=n):
        p = np.array(per, int)
        if k_count(p, n) == k:
            unique = 1
            for uni in eq_list:
                if eq_check(p, uni, n) == 1:
                    unique = 0
                    break
            if unique == 1:
                eq_list.append(p)
                eq_counter += 1
    sym_counter = 0
    p = 0
    for c_eq in eq_list:
        sym = sym_check(c_eq, n)
        if sym > 0:
            sym_counter += 1
    print('Классов эквивалентности -- симметричных: ', eq_counter, ' -- ', sym_counter)


# f = open('result.csv', 'w')


def main():
    n = int(input('Введите количество цифр - '))
    k = int(input('Введите количество единиц - '))

    # for n in range(6, 16):
    #     for k in range(3, int(n / 2) + 1):
    #         print('Количество цифр -- количество единиц: ', n, ' -- ', k, ':', file=f)

    eq(n, k)


if __name__ == '__main__':
    main()


# f.close()