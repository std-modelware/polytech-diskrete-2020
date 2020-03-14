import numpy as math


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
    counter = 0
    for ksi in range(max_len, 2 * digits - max_len - 1 if digits % 2 == 1 else max_len + digits // 2):
        i = 1
        while number[ksi - i] == number[ksi + i]:
            if i == max_len:
                counter += 1
                break
            i += 1
    if digits % 2 == 0:
        max_len = digits // 2
        for ksi in range(max_len, max_len + digits // 2):
            i = 1
            j = 0
            while number[ksi + j] == number[ksi - i]:
                if i == max_len:
                    counter += 1
                    break
                i += 1
                j += 1
    return counter


numbers = [0b1010, 0b10110, 0b11111, 0b110011, 0b110101, 0b111111, 0b1011010]
for n in numbers:
    print('Axis in ', bin(n), ': ', count_sym_axis(n))
print('Axis in ', bin(0b000000), ': ', count_sym_axis(0b000000, 6))
