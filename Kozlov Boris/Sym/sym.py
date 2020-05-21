import matplotlib.pyplot as plot
import numpy as math
import os
import shutil

"""
Примитивная функция, считающая количество 1 в двоичной записи десятичного числа.
"""
def count_ones(number):
    quantity = 0
    while number > 0:
        quantity += number & 1
        number >>= 1
    return quantity


"""
Функция, реализующая циклический сдвиг вправо на заданное количество шагов.
"""
def shift(number, step):
    temp = ''
    while number > 0:
        temp += str(number % 2)
        number //= 2
    number_list = list(reversed(temp))
    for i in range(step):
        number_list.insert(0, number_list.pop())
    return int("".join(number_list), 2)


"""
Функция, выделяющая из множества чисел заданной длины и 
с заданным количеством единиц в двоичной записи подмножество таких чисел,
из которых могут быть получены все другие числа множества путем циклического сдвига.
Сами числа подмножества не могут быть получены друг из друга таким путем.
"""
def create_unique_number_sequences(len, ones):
    answer = []
    full_set = []
    for number in range(2 ** (len - 1), 2 ** len):
        if count_ones(number) == ones and number not in full_set:
            answer.append(number)
        temp = number
        for step in range(1, len):
            full_set.append(temp)
            temp = shift(number, step)
    return answer


"""
Функция, считающая, относительно скольких осей симметрии в правильном многоугольнике, значения в
вершинах которого могут принимать значения 0 или 1, и чьи вершины 
образуют последовательность, являющуюся записью введенного числа в двоичной
системе, подпоследовательности вершин с двух сторон совпадают. Оси симметрии 2n-угольника могут
проходить через противоположные вершины или через середины двух противоположных сторон, в то время
как у (2k+1)-угольника они могут проходить только через вершину и середину противоположной стороны.
"""
def count_axis_in_sequence(number):
    quantity = 0
    temp = ''
    is_vertex_with_ax = []
    is_midpoint_with_ax = []
    while number > 0:
        temp += str(number % 2)
        number //= 2
    number_list = list(reversed(temp))
    len_list = temp.__len__()
    is_subsequence = 0
    if len_list % 2 == 0:
        sub_len = int((len_list - 2) / 2)
        for i in range(sub_len + 1):
            is_subsequence = 1
            for j in range(1, sub_len + 1):
                if number_list[i - j] != number_list[i + j]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
                is_vertex_with_ax.append(i)
        sub_len = int(len_list / 2)
        for i in range(sub_len):
            is_subsequence = 1
            for j in range(sub_len):
                if number_list[i - j] != number_list[i + 1 + j]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
                is_midpoint_with_ax.append(i)
    else:
        sub_len = int((len_list - 1) / 2)
        for i in range(len_list):
            is_subsequence = 1
            for j in range(1, sub_len + 1):
                if number_list[(i - j) % len_list] != number_list[(i + j) % len_list]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
                is_vertex_with_ax.append(i)
    return quantity, is_vertex_with_ax, is_midpoint_with_ax


"""
Функция, рисующая правильный многоугольник и нужные оси симметрии.
"""
def draw_polygon(number, is_vertex_with_ax, is_midpoint_with_ax):
    temp = ''
    while number > 0:
        temp += str(number % 2)
        number //= 2
    number_list = list(reversed(temp))
    len_list = temp.__len__()
    x = []
    y = []
    plot.figure(figsize=(6, 6))
    x.append(1)
    y.append(0)
    for i in range(1, len_list):
        coord_x = math.cos(2 * math.pi * i / len_list)
        coord_y = math.sin(2 * math.pi * i / len_list)
        x.append(coord_x)
        y.append(coord_y)
        plot.plot([x[i - 1], x[i]], [y[i - 1], y[i]], c='r')
    plot.plot([x[-1], x[0]], [y[-1], y[0]], c='r')
    for i in range(len_list):
        if number_list[i] == '1':
            plot.scatter(x[i], y[i], c='r', s= 75)
        else:
            plot.scatter(x[i], y[i], c='w', edgecolors='r', s=75)
    if len_list % 2 == 0:
        sub_len = int((len_list - 2) / 2)
        for i in range(sub_len + 1):
            if i in is_vertex_with_ax:
                x_end = math.cos(2 * math.pi * i / len_list + math.pi)
                y_end = math.sin(2 * math.pi * i / len_list + math.pi)
                plot.plot([x[i], x_end], [y[i], y_end], ls=':', lw=4)
        sub_len = int(len_list / 2)
        for i in range(sub_len):
            if i in is_midpoint_with_ax:
                x_start = math.cos(2 * math.pi * (i + 1/2) / len_list)
                y_start = math.sin(2 * math.pi * (i + 1/2) / len_list)
                x_end = math.cos(2 * math.pi * (i + 1/2) / len_list + math.pi)
                y_end = math.sin(2 * math.pi * (i + 1/2) / len_list + math.pi)
                plot.plot([x_start, x_end], [y_start, y_end], ls=':', lw=4)
    else:
        for i in range(len_list):
            if i in is_vertex_with_ax:
                x_end = math.cos(2 * math.pi * i / len_list + math.pi)
                y_end = math.sin(2 * math.pi * i / len_list + math.pi)
                plot.plot([x[i], x_end], [y[i], y_end], ls=':', lw=4)
    plot.grid(True)


"""
Предполагается, что заданное множество содержит
элементы по крайней мере с 1 единицей в записи.
Если же нет, то, очевидно, что вводимый нуль длины
n образует многоугольник, у которого относительно всех
осей симметрии будет наблюдаться совпадение подпоследовательностей
с обеих сторон.
"""
len = int(input("Enter the sequence's length: "))
num_of_ones = int(input("Enter the number of ones: "))
if len >= 3 and num_of_ones > 0:
    path = os.getcwd() + "\\plots"
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir("plots")
    sequences = create_unique_number_sequences(len, num_of_ones)
    for sequence in sequences:
        quantity, num1, num2 = count_axis_in_sequence(sequence)
        if quantity > 0:
            draw_polygon(sequence, num1, num2)
            plot.savefig(fname=path + "\\AxisOf" + str(sequence) + ".png", dpi=100)
            plot.close()
        print(str(bin(sequence)) + " is a unique sequence,")
        print("It has " + str(quantity) + " axis of symmetry overall.\n")
elif len >= 3 and num_of_ones == 0:
    path = os.getcwd() + "\\plots"
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir("plots")
    quantity, num1, num2 = count_axis_in_sequence(2 ** len - 1)
    draw_polygon(2 ** len - 1, num1, num2)
    plot.savefig(fname=path + "\\AxisOf" + str(0) + ".png", dpi=100)
    plot.close()
    print("0b".ljust(len + 2, '0') + " is the only sequence possible,")
    print("It has " + str(quantity) + " axis of symmetry overall.\n")
else:
    print("Incorrect input, please try again.")
