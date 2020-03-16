import numpy as math
import matplotlib.pyplot as plot


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
    plot.scatter(x_zer, y_zer, c='w', edgecolors='b')
    plot.scatter(x_one, y_one, c='b')
    plot.plot(x, y, c='b')
    plot.plot([x[0], x[-1]], [y[0], y[-1]], c='b')
    axis = count_sym_axis(number, digits)
    for i in axis:
        x_a, y_a = get_axi_coord(digits, i)
        plot.plot(x_a, y_a, ls=':')


numbers = [0b1010, 0b10110, 0b11111, 0b110011, 0b110101, 0b111111, 0b1011010]
# numbers = [0b110011, 0b110101, 0b111111]
for n in numbers:
    sym_axis = count_sym_axis(n)
    print('Axis in ', bin(n), ': ', sym_axis)
    draw_poly(n)
plot.show()
