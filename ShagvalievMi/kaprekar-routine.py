import pandas as pd
import numpy as np
import enum


class Error(enum.Enum):
    ERROR_OK = 0
    ERROR_NUM_OVER = 1


def kaprekar(number_list, digits_n, base):
    max_num = convert_list_to_int(list(sorted(number_list)), digits_n, base)
    min_num = convert_list_to_int(list(sorted(number_list, reverse = True)), digits_n, base)
    new_num = max_num - min_num
    err, new_num_list = convert_int_to_list(new_num, digits_n, base)
    return new_num_list


def convert_int_to_list(number_int, digits_n, base):
    num_list = []
    if number_int == 0:
        num_list = [0 for i in range(digits_n)]
        return Error.ERROR_OK, num_list
    actual_number_of_digits = 1
    while number_int > 0:
        if actual_number_of_digits > digits_n:
            return Error.ERROR_NUM_OVER, num_list
        number_int, mod = divmod(number_int, base)
        actual_number_of_digits += 1
        num_list.append(mod)
    for i in range(actual_number_of_digits, digits_n+1):
        num_list.append(0)
    return Error.ERROR_OK, num_list


def convert_list_to_int(number_list, digits_n, base):
    number = 0
    for i in range(digits_n):
        number += number_list[i] * (base ** i)
    return number


def generate_next_unique_number(prev_num, digits_n, base):
    new_num = prev_num.copy()
    i = 0
    while new_num[i]+1 > base - 1:
        i = i + 1
        if i == digits_n:
            return Error.ERROR_NUM_OVER, new_num
    new_num[i] += 1
    for j in range(i-1, -1, -1):
        new_num[j] = new_num[i]
    return Error.ERROR_OK, new_num


def main():
    #testing
    num_list = [4, 9, 5]
    num_list.reverse()
    digits_n = 3
    base = 10
    new_num_list = kaprekar(num_list, digits_n, base)
    print(list(reversed(new_num_list)))


main()
