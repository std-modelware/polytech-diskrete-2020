import sys
import numpy as np
import matplotlib.pyplot as plt


# Отрисовываем ось симметрии, если таковая имеется.
# Битовую последовательность представляем в виде окружности
def polygon(arr, r: int, intersect: int, mod: int):
    x = [0] * (r + 1)
    y = [0] * (r + 1)
    rot = 2 * np.pi / r

    t = np.arange(0, 2 * np.pi, 0.01)
    radius = 1
    plt.plot(radius * np.sin(t), radius * np.cos(t), color="r", linewidth=0.5)
    plt.grid(color="grey", which="both", linestyle="--", linewidth=0.5)
    plt.title(arr)

    for i in range(r + 1):
        x[i] = np.cos(i * rot + np.pi / 2)
        y[i] = np.sin(i * rot + np.pi / 2)

    for i in range(r):
        plt.text(x[i], y[i] - 0.1, arr[i], color="green")
        if arr[i] == '1':
            plt.scatter(x[i], y[i], s=20, color="navy")
        else:
            plt.scatter(x[i], y[i], s=20, color="red")

    # Рисуем линию симметрии (Есть три случая, которые описаны в функции, вызывающей метод polygon)
    if intersect > 0:
        k = 1
    else:
        k = 0
    if mod == 1:
        plt.plot([x[intersect], x[((r+1)//2 + intersect) % r]], [y[intersect], y[(r//2 + intersect) % r]],
                 color="darkmagenta", linewidth=0.8)
    elif mod == 2:
        plt.plot([(x[(intersect - k) % r] + x[(intersect ) % r]) * 0.75,
                  (x[(r//2 + intersect - k) % r] + x[(r//2 + intersect) % r]) * 0.75],
                 [(y[(intersect - k) % r] + y[(intersect) % r]) * 0.75,
                  (y[(r//2 + intersect - k) % r] + y[(r//2 + intersect) % r]) * 0.75],
                 color="darkmagenta", linewidth=0.8)
    elif mod == 3:
        plt.plot([x[intersect], (x[(r//2 + intersect) % r] + x[(r//2 + intersect + 1) % r]) / 2],
                 [y[intersect], (y[(r//2 + intersect) % r] + y[(r//2 + intersect + 1) % r]) / 2],
                 color="darkmagenta", linewidth=0.8)

    plt.show()


# Генератор перестановок (создаем новый список посредством смены индексации исходного массива)
def supp_permut(array, r=None):
    iterat = array
    size = len(iterat)

    r = size if r is None else r
    if r > size:
        return

    index = [i for i in range(size)]
    cycle = [i for i in range(size, size-r, -1)]

    yield list(iterat[i] for i in index[:r])
    while size:
        for i in reversed(range(r)):
            cycle[i] -= 1
            if cycle[i] == 0:
                index[i:] = index[i+1:] + index[i:i+1]
                cycle[i] = size - i
            else:
                j = cycle[i]
                index[i], index[-j] = index[-j], index[i]
                yield list(iterat[i] for i in index[:r])
                break
        else:
            return


# Проверяем: является ли новая перестановка циклическим сдвигом или нет
def check_per(list_num, array, r: int):
    temp: list = [0] * r
    k: int = 0

    while k < r:
        for i in range(r):
            temp[i] = array[(i + k) % r]

        if temp in list_num:
            return False
        k += 1

    return True


# Создаем первоначальный массив, заполненный нулями и единицами
def create_sequentially(n: int, k: int):
    string = "1" * k
    string += "0" * (n-k)

    return string


def find_sym(arr, size):  # Находим и подсчитываем количество симметрий для данной последовательности
    elem = np.concatenate([arr, arr])

    # Случай, когда размер массива четный
    if size % 2 == 0:
        step = k = size // 2

        if k == 1:
            if elem[0] != elem[1]:
                yield tuple([elem[0], elem[1], 2])

        # Проводим линию по точкам (по диаметру) mod(случай) = 1
        for i in range(0, k):
            fir = elem[i + 1: k + i]
            sec = elem[k + i + 1: k + i + step]
            if np.array_equal(np.flipud(fir), sec):
                polygon(arr, size, i, 1)
                yield tuple([fir, sec, 1])

        # Проводим между точками mod(случай) = 2
        for i in range(0, k):
            fir = elem[i:k + i]
            sec = elem[k + i: i + k + step]
            if np.array_equal(np.flipud(fir), sec):
                polygon(arr, size, i, 2)
                yield tuple([fir, sec, 2])

    # Нечетный случай, тогда линия пройдет через точку и между двумя точками mod(случай) = 3
    elif size % 2 == 1:
        k = size
        step = size // 2

        for i in range(0, k):
            fir = elem[i + 1: step + i + 1]
            sec = elem[step + i + 1: i + 2 * step + 1]
            if np.array_equal(np.flipud(fir), sec):
                polygon(arr, size, i, 3)
                yield tuple([fir, sec, 3])


# В файл записываем исходную битовую последовательность, симметричные подпоследовательности (3 случая) и количество
# симметрий в данной последовательности
def add_to_analys(list_num: list, n: int, file):
    for i in list_num:
        sym_count = 0
        file.write(str(i) + " : bit array\n")
        for j in find_sym(i, n):
            if j[2] == 1:
                file.write("Through two numbers, case 1: \n")
            elif j[2] == 2:
                file.write("Between numbers, case 2: \n")
            else:
                file.write("Number - between number, case 3: \n")
            file.write(str(j[0]) + " | " + str(j[1]) + "\n")
            sym_count += 1

        file.write("Total sym count: {:d}\n".format(sym_count))
        file.write("\n")


def main():
    # Задаем первичные значения
    n = 6
    k = 2
    list_num: list = []

    for i in supp_permut(create_sequentially(n, k), n):
        if check_per(list_num, i, n):
            list_num.append(i)

    try:
        file = open("result.txt", "w")
    except IOError:
        print("Could not open file!")

    add_to_analys(list_num, n, file)
    print(type(file))
    file.close()


if __name__ == "__main__":
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main()
