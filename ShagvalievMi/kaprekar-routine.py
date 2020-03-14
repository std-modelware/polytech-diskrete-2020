import pandas as pd
import numpy as np
import enum


# digits_n - number of digits in number
# base - numeral system
# num_int - natural number represented as integer
# num_list - number in a certain numeral system (base) w certain number of digits (digits_n) represented as list


# function of creating DataFrame out of strings representing Im(<x>, d, r> for each 1<d<=max_digits_n and 1<r<=max_base
# input is max numeral system (max_base) and max number of digits (max_digits_n)
# output is DataFrame (table)
def build_table(max_base, max_digits_n):
    matrix = np.empty((max_base - 1, max_digits_n - 1), dtype='U40')    # numpy 2D array of strings
    for base in range(2, max_base+1):
        for digits_n in range(2, max_digits_n+1):
            im = ImKaprekar(digits_n, base)
            str_im = 'const.p.' + str(len(im.const_points)) + ' loop.' + str(len(im.loops)) + ' max.l.' + str(im.max_len_loop) + ' max.w.' + str(im.max_len_way)
            # const.p is number of const points, loop is number of loops, max.l is max length of loop, max.w. is max way
            matrix[base-2][digits_n-2] = str_im
    table = pd.DataFrame(matrix, index=[str(b) + ' base' for b in range(2, max_base + 1)],
                              columns=[str(d) + ' digits' for d in range(2, max_digits_n + 1)])
    # pandas DataFrame (table)
    return table


# class ImKaprekar, representing Im of Kaprekar({num}, digits_n, base)
class ImKaprekar:

    # digits_n
    # base
    # max_len_way       max number of elements in required to get to the loop or const point
    # max_len_loop      max number of elements in loop
    # const_points      constant points list of num_ints
    # loops     loops list, each element of list is some num_int from it's loop

    # method of adding constant point and way to it
    # adds const point if its new, else ignores
    # if len_way > max_len_way sets max_len_way to len_way
    # input is constant point to be added as int (new_const_point) and length of way to it (len_way)
    def __add_const_point_w_way(self, new_const_point, len_way):
        self.max_len_way = max(self.max_len_way, len_way)
        if self.const_points.count(new_const_point):
            return
        self.const_points.append(new_const_point)

    # method of adding loop and way to it
    # adds first elem of loop to loops list if its new loop, else ignores
    # if len_way > max_len_way sets max_len_way to len_way
    # input is loop to be added as list of num_int (new_loop) and length of way to it (len_way)
    def __add_loop_w_way(self, new_loop, len_way):
        self.max_len_way = max(self.max_len_way, len_way)
        for cur_elem in new_loop:
            if self.loops.count(cur_elem):
                return
        self.loops.append(new_loop[0])
        self.max_len_loop = max(self.max_len_loop, len(new_loop))

    # method of initializing object of class ImKaprekar
    # sets digits_n and base
    # finds all constant points and stores them in list (const_points)
    # finds all loops and stores some element of them in list (loops)
    # finds max length of loop (max_len_loop)
    # finds max length of way to loop or const point (max_len_way)
    # input is number of digits (digits_n) and numerical system (base)
    def __init__(self, digits_n, base):
        self.loops = []
        self.const_points = []
        self.max_len_loop = self.max_len_way = 0
        self.digits_n = digits_n
        self.base = base
        start_num_int = 0
        err, start_num_list = convert_int_to_list(start_num_int, digits_n, base)
        num_list = start_num_list.copy()
        err = Error.ERROR_OK
        while err == Error.ERROR_OK:
            len_way, loop = build_kaprekar_sequence(num_list, digits_n, base)
            if len(loop) == 1:
                self.__add_const_point_w_way(loop[0], len_way)
            else:
                self.__add_loop_w_way(loop, len_way)
            err, num_list = generate_next_unique_number(num_list, digits_n, base)


# error enum
class Error(enum.Enum):
    ERROR_OK = 0
    ERROR_NUM_OVER = 1


# function of building kaprekar sequence and detecting loops,
# example of sequence for num = 1100, digits_n = 4, base = 10:
# 1100->1089->9621->8352->6174
# input is number as list (number_list) with (digits_n) digits in numeral system (base)
# output is number of elements before the loop (len_way) and loop (loop)
def build_kaprekar_sequence(number_list, digits_n, base):
    len_way = 0     # number of elements in sequence but not in cycle
    len_loop = 0    # number of elements in cycle
    sequence = []   # current kaprekar sequence, each element of sequence is num_int
    num_int = convert_list_to_int(number_list, digits_n, base)
    sequence.append(num_int)
    new_number_list = number_list.copy()    # number to be iterated
    while True:
        new_number_list, new_number_int = kaprekar(new_number_list, digits_n, base)
        if sequence.count(new_number_int):
            len_way = sequence.index(new_number_int)
            len_loop = len(sequence) - len_way
            break
        else:
            sequence.append(new_number_int)
    loop = sequence[-len_loop:]     # detected loop (m.b. out of 1 element)
    return len_way, loop


# kaprekar function, computes new_num by sorting digits of input number
# in ascending and descending order and then subtracting them
# input is number as list (num_list), number of digits (digits_n) and base (base)
# output is new_num as list (new_num_list) and as int (new_num_int)
def kaprekar(num_list, digits_n, base):
    max_num_int = convert_list_to_int(list(sorted(num_list)), digits_n, base)
    # max number constructed out of sorted digits of input number
    min_num_int = convert_list_to_int(list(sorted(num_list, reverse=True)), digits_n, base)
    # min number constructed out of sorted digits of input number
    new_num_int = max_num_int - min_num_int     # new number ( K(i, d, r) )
    err, new_num_list = convert_int_to_list(new_num_int, digits_n, base)
    return new_num_list, new_num_int


# function of converting number from int form to list form
# input is number as int (num_int), number of digits (digits_n) and base (base)
# output is error flag (err), number as list (num_list) with (digits_n) digits in numeral system (base)
def convert_int_to_list(num_int, digits_n, base):
    num_list = []
    if num_int == 0:
        num_list = [0] * digits_n
        return Error.ERROR_OK, num_list
    actual_number_of_digits = 1     # "real" number of digits in representation of num_int
    # in a certain numeral system (base) w certain number of digits (digits_n)
    while num_int > 0:
        if actual_number_of_digits > digits_n:
            return Error.ERROR_NUM_OVER, num_list
        num_int, mod = divmod(num_int, base)
        actual_number_of_digits += 1
        num_list.append(mod)
    for i in range(actual_number_of_digits, digits_n+1):
        num_list.append(0)
    return Error.ERROR_OK, num_list


# function of converting number from list form to int form
# input is number as list (number_list) with (digits_n) digits in numeral system (base)
# output is number as int (num_int)
def convert_list_to_int(number_list, digits_n, base):
    num_int = 0
    for i in range(digits_n):
        num_int += number_list[i] * (base ** i)
    return num_int


# function of generating number constructed out of unique set of digits
# used to reduce amount of numbers to be processed
# set of digits in output number is different from set of digits in input number (and previous numbers)
# by applying this function to 0 and then iterating output, we get set of numbers
# all constructed out of unique sets of numbers
# input is number as list (prev_num_list) with (digits_n) digits in numeral system (base)
# output is error flag, next number as list (new_num_list)
def generate_next_unique_number(prev_num_list, digits_n, base):
    new_num_list = prev_num_list.copy()
    i = 0
    while new_num_list[i]+1 > base - 1:
        i = i + 1
        if i == digits_n:
            return Error.ERROR_NUM_OVER, new_num_list
    new_num_list[i] += 1
    for j in range(i-1, -1, -1):
        new_num_list[j] = new_num_list[i]
    return Error.ERROR_OK, new_num_list


# main function
def main():
    digits_n = 8
    base = 16
    table = build_table(base, digits_n)
    table
    

main()
