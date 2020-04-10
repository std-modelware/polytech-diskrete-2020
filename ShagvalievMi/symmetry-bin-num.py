import matplotlib.pyplot as plt
import numpy.matlib as np
import math


#   прямая, проходящая через (0,0) и (x1,y1)
def straight_line_centre_and_point(x, x1, y1):
    return x*y1/x1


#   Рисовка двоичного числа как многоугольника
def draw_polygon_binary_num(radius, num_list):
    x = []
    y = []
    val_to_move_num = 1
    angles = np.linspace(0, 2*math.pi, len(num_list)+1)
    for cur_angle in angles:
        y.append(radius*math.cos(cur_angle))
        x.append(radius*math.sin(cur_angle))
    for i in range(len(num_list)):
        plt.text(x[i]+val_to_move_num*my_sign(x[i]), y[i]+val_to_move_num*my_sign(y[i]), str(num_list[i]))
    plt.plot(x, y, '-', color='#4CB2DC', linewidth=3)
    plt.plot(x, y, '.', color='black', markersize=10)
    plt.ylim([-radius - val_to_move_num, radius + val_to_move_num])
    plt.xlim([-radius - val_to_move_num, radius + val_to_move_num])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.title(str(num_list).strip('[]'), loc='left')


#   Рисовка осей симметрии
def draw_sym_axis_binary_num(radius, num_list, sym_list):
    angles = np.linspace(0, 2 * math.pi, len(num_list) + 1)
    for cur_sym_node in sym_list:
        if isinstance(cur_sym_node, int):
            x = radius*math.sin(angles[cur_sym_node])
            y = radius*math.cos(angles[cur_sym_node])
        if isinstance(cur_sym_node, tuple):
            angle = (angles[cur_sym_node[1]] + angles[cur_sym_node[0]]) / 2
            x = radius * math.sin(angle)
            y = radius * math.cos(angle)
        if x == 0:
            x_line = 0
            y1_line = 50
            y2_line = -50
        else:
            x_line = 50
            y1_line = straight_line_centre_and_point(x_line, x, y)
            y2_line = straight_line_centre_and_point(-x_line, x, y)
        plt.plot((-x_line, x_line), (y2_line, y1_line), '--', color='black', linewidth=1)


#   Проходит ли через позицию i ось симметрии
def check_sym_from_node(num_list, i):
    n = len(num_list)
    i_right = i_left = i
    for cur_step in range(math.floor(n/2)):
        i_right = my_inc(i_right, n)
        i_left = my_dec(i_left, n)
        if num_list[i_left] != num_list[i_right]:
            return 0
    return 1


#   Проходит ли между позициями left и right ось симметрии
def check_sym_from_pair(num_list, left, right):
    n = len(num_list)
    i_right = right
    i_left = left
    for cur_step in range(math.floor(n/2)):
        if num_list[i_left] != num_list[i_right]:
            return 0
        i_right = my_inc(i_right, n)
        i_left = my_dec(i_left, n)
    return 1


#   Поиск всех осей симметрии числа
def find_all_sym_axis(num_list):
    sym_list = []
    n = len(num_list)
    if n % 2 == 0:
        for i in range(math.floor(n/2)):
            if check_sym_from_node(num_list, i):
                sym_list.append(i)
            if check_sym_from_pair(num_list, i, i+1):
                sym_list.append((i, i+1))
    else:
        for i in range(n):
            if check_sym_from_node(num_list, i):
                sym_list.append(i)
    return sym_list


#   Класс "уникальных чисел" (aka ожерелий (англ. necklaces))
#   public var: n, k, necklaces(list)
class BinaryNecklaces:

    #   Генерация ожерелий, вызывается в конструкторе
    #   Реализация основана на статье:
    #   https://www.sciencedirect.com/science/article/pii/S0304397503000495
    def __simple_fixed(self, t, p):
        if t > self.n:
            if self.n % p == 0:
                # print(self.cur_number)
                self.necklaces.append(self.__cur_number.copy())
        else:
            for digit in range(self.__cur_number[t - p - 1], 2):
                if self.__amount_of_zeros_and_ones[digit] > 0:
                    self.__cur_number[t - 1] = digit
                    self.__amount_of_zeros_and_ones[digit] -= 1
                    if digit == self.__cur_number[t - p - 1]:
                        self.__simple_fixed(t + 1, p)
                    else:
                        self.__simple_fixed(t + 1, t)
                    self.__amount_of_zeros_and_ones[digit] += 1

    def __init__(self, _n, _k):
        self.n = _n
        self.k = _k
        self.necklaces = []

        self.__cur_number = [0] * self.n
        self.__amount_of_zeros_and_ones = [self.n - self.k, self.k] # n-k нулей, k единиц
        self.__simple_fixed(1, 1)


def my_inc(i, n):
    return (i+1) % n


def my_dec(i, n):
    return i - 1


def my_sign(x):
    if math.fabs(x) < 1.e-10:
        return 0
    if x > 0:
        return 1
    return -1


#   Вывод только чисел с осями симметрии в файл res
def main():
    file_res = open("res.txt", "w")
    n = int(input("Number of digits, n: "))
    k = int(input("Number of ones, k: "))
    print("Number of digits, n:", n, " Number of ones, k:", k, "\n", file=file_res)
    obj_necklaces = BinaryNecklaces(n, k)
    total_sum = 0
    necklaces_list = obj_necklaces.necklaces
    for num in necklaces_list:
        sym_axes = find_all_sym_axis(num)
        if len(sym_axes):
            print(*num, sep=" ", end='| num of sym axis: ', file=file_res)
            print(len(sym_axes), file=file_res)
            draw_polygon_binary_num(10, num)
            draw_sym_axis_binary_num(10, num, sym_axes)
            plt.show()
        total_sum += len(sym_axes)
    print('total num of sym axis: ', total_sum, file=file_res)


main()
