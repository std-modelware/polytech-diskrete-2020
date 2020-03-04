import time
import cProfile
# import pywin32


def dec(list_from_number, r):
    number = 0
    for k in range(len(list_from_number)):
        # number += list_from_number[len(list_from_number) - k - 1] * r ** k
        number *= r
        number += int(list_from_number[k], r)
    return number


def convTo(number, r):
    alphabet = "0123456789ABCDEF"
    div, mod = divmod(number, r)
    if number < r:
        return alphabet[number]
    return convTo(div, r) + alphabet[mod]


def kaprekar(number, d, r):
    number_str = str(number)
    number_str = number_str.rjust(d, '0')
    list_from_number = list(number_str)
    list_from_number.sort(key=lambda ch: int(ch, r))
    min_num = dec(list_from_number, r)
    list_from_number.reverse()
    max_num = dec(list_from_number, r)
    return convTo(max_num - min_num, r)


def findMagicNumbers(d, r):
    max_number = r ** d
    magic_numbers = []
    for i in range(max_number):
        i_str = convTo(i, r)
        tmp = kaprekar(i_str, d, r)
        if i_str == tmp:
            magic_numbers.append(tmp)
    return magic_numbers


def findCycleLength(d, r):
    length = 0
    max_number = r ** d
    for i in range(max_number):
        cur_length = 0
        list_cycle = []
        i_str = convTo(i, r)
        # print(i_str)
        list_cycle.append(i_str)
        last_num = kaprekar(i_str, d, r)
        while last_num not in list_cycle:
            cur_length += 1
            list_cycle.append(last_num)
            last_num = kaprekar(last_num, d, r)
        if cur_length > length:
            length = cur_length
    return length


startTime = time.time()
# pr = cProfile.Profile()
# pr.enable()
num_sys_lim = 10
digits_lim = 6
'''for i in range(1, digits_lim + 1):
    for j in range(2, num_sys_lim + 1):
        print(i, "digits", j, "system:", findCycleLength(i, j), "|| magic numbers: ", findMagicNumbers(i, j))'''
file = open('table.csv', 'w')
file.write('digits;system;max steps before magic number or cycle;magic numbers\n')
for i in range(1, digits_lim + 1):
    for j in range(2, num_sys_lim + 1):
        file.write('%i;%i;%i;%s\n' % (i, j, findCycleLength(i, j), findMagicNumbers(i, j)))
file.close()

# pr.disable()
# pr.print_stats()
print("--- %s sec. ---" % (time.time() - startTime))