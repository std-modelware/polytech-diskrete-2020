import time


def dec(list_from_number, r):
    number = 0
    for k in range(len(list_from_number)):
        number += list_from_number[len(list_from_number) - k - 1] * r ** k
    return number


def convTo(number, r):
    alphabet = "0123456789ABCDEF"
    div, mod = divmod(number, r)
    if number < r:
        return alphabet[number]
    return convTo(div, r) + alphabet[mod]


def kaprekar(number, d, r):
    number_str = str(number)
    while len(number_str) < d:
        number_str = '0' + number_str
    list_from_number = [int(ch, r) for ch in number_str]
    list_from_number.sort()
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
num_sys_lim = 16 + 1
digits_lim = 4 + 1
for i in range(1, digits_lim):
    for j in range(2, num_sys_lim):
        print(i, "digits", j, "system:", findCycleLength(i, j), "|| magic numbers: ", findMagicNumbers(i, j))
print("--- %s sec. ---" % (time.time() - startTime))