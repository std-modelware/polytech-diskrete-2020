import numpy as math
import matplotlib.pyplot as plot
import os
import shutil

def count_digits(number):
    return int(math.log2(number) + 1)


def long_array_of_num(number, digits):
    res = []
    for i in range(digits - 1, -1, -1):
        res.append(number >> i & 1)
    res = res + res
    return res


def count_sym_axis(number, digits=0):
    if digits == 0:
        digits = count_digits(number)
    number = long_array_of_num(number, digits)
    max_len = digits // 2 if digits % 2 == 1 else (digits - 2) // 2
    axis = []
    for ksi in range(max_len, 2 * digits - max_len - 1 if digits % 2 == 1 else max_len + digits // 2):
        i = 1
        while number[ksi - i] == number[ksi + i]:
            if i == max_len:
                axis.append(ksi % digits)
                break
            i += 1
    if digits % 2 == 0:
        max_len = digits // 2
        axis = [(n * 2) % digits for n in axis ]
        for ksi in range(max_len, max_len + digits // 2):
            i = 1
            j = 0
            while number[ksi + j] == number[ksi - i]:
                if i == max_len:
                    axis.append((2 * ksi  - 1) % digits)
                    break
                i += 1
                j += 1
    return axis


def ones_zeros_ind(number, digits=0):
    if digits == 0:
        digits = count_digits(number)
    res = [[],[]]
    for i in range(digits):
        if number >> i & 1 == 0:
            res[0].append(digits - i - 1)
        else:
            res[1].append(digits - i - 1)
    return res


def get_poly_points(n, r=1):
    x = []
    y = []
    angle = math.pi - (n-2) * math.pi / n
    for i in range(n):
        x.append(r * math.cos(i * angle))
        y.append(r * math.sin(i * angle))
    return x, y


def get_axi_coord(n, ax_num, r=1):
    x = []
    y = []
    angle = math.pi - (n - 2) * math.pi / n
    if n % 2 == 0:
        ax_num = ax_num / 2
    x.append(r * math.cos(ax_num * angle))
    y.append(r * math.sin(ax_num * angle))
    x.append(r * math.cos((ax_num + n / 2) * angle))
    y.append(r * math.sin((ax_num + n / 2) * angle))
    return x, y


def draw_poly(number, digits=0):
    if digits == 0:
        digits = count_digits(number)
    x, y = get_poly_points(digits)
    filter = ones_zeros_ind(number)
    x_zer = []
    y_zer = []
    x_one = []
    y_one = []
    for i in filter[0]:
        x_zer.append(x[i])
        y_zer.append(y[i])
    for i in filter[1]:
        x_one.append(x[i])
        y_one.append(y[i])
    plot.figure(figsize=(6,6))
    plot.plot(x, y, c='b')
    plot.plot([x[0], x[-1]], [y[0], y[-1]], c='b')
    plot.scatter(x_zer, y_zer, c='w', edgecolors='b', s=100)
    plot.scatter(x_one, y_one, c='b', s=100)
    axis = count_sym_axis(number, digits)
    for i in axis:
        x_a, y_a = get_axi_coord(digits, i)
        plot.plot(x_a, y_a, ls=':', lw=2.5)


def rotate_right(n, num):
    mask = 2 ** (n - 1) if num & 1 == 1 else 0
    num = num >> 1 | mask
    return num


def count_ones(n, num):
    counter = 0
    for i in range(n):
        counter += 1 if num & (2 ** i) > 0 else 0
    return counter


def gen_nums(n, k):
    full_list = []
    res = []
    for cur in range(2 ** (n - 1), 2 ** n):
        if count_ones(n, cur) == k:
            if cur not in full_list:
                res.append(cur)
                tmp = cur
                for j in range(k):
                    full_list.append(tmp)
                    tmp = rotate_right(n, tmp)
    return res


#n = 8 #number of digits
#k = 4 #number of ones
#dpi = 75 #quality of images
print("Enter the number of digits: ")
n = int(input())
print("Enter the number of ones: ")
k = int(input())
print("Enter the dpi of exported figures: ")
dpi = int(input())
if n >= 3 and k >= 1 and k <= n and n <= 36 and dpi >= 75:
    path = os.getcwd() + "\\plots"
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir("plots")
    numbers = gen_nums(n, k)
    for n in numbers:
        sym_axis = count_sym_axis(n)
        print('Axis in ', bin(n), ': ', sym_axis)
        draw_poly(n)
        plot.savefig(fname= path + "\\poly" + str(n) + ".png", dpi=dpi)
        plot.close()
else:
    print("Enter the correct parameters!")
