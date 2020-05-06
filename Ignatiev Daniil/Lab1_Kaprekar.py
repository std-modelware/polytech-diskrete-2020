import cProfile

def dec(NUMBERS, t):
    number = 0
    for k in range(len(NUMBERS)):
        number *= t
        number += int(NUMBERS[k], t)
    return number


def Transform(number, t):
    symbols = "0123456789ABCDEF"
    div, mod = divmod(number, t)
    if number < t:
        return symbols[number]
    return Transform(div, t) + symbols[mod]


def kaprekar(number, d, t):
    number_str = str(number)
    number_str = number_str.rjust(d, '0')
    NUMBERS = list(number_str)
    NUMBERS.sort(key=lambda ch: int(ch, t))
    min_num = dec(NUMBERS, t)
    NUMBERS.reverse()
    max_num = dec(NUMBERS, t)
    return Transform(max_num - min_num, t)


def MagicNumbers(d, t):
    max_number = t ** d
    magic_numbers = []
    for i in range(max_number):
        i_str = Transform(i, t)
        tmp = kaprekar(i_str, d, t)
        if i_str == tmp:
            magic_numbers.append(tmp)
    return magic_numbers


def CycleLength(d, t):
    length = 0
    max_number = t ** d
    for i in range(max_number):
        cur_length = 0
        CYCLE = []
        i_str = Transform(i, t)
        CYCLE.append(i_str)
        last_num = kaprekar(i_str, d, t)
        while last_num not in CYCLE:
            cur_length += 1
            CYCLE.append(last_num)
            last_num = kaprekar(last_num, d, t)
        if cur_length > length:
            length = cur_length
    return length


LimitSystems = 10
LimitDigits = 6
file = open('result.csv', 'w')
file.write('"digits","digit_system","max_steps","magic_numbers"\n')
for i in range(1, LimitDigits + 1):
    for j in range(2, LimitSystems + 1):
        file.write('       %i     		          %i               %i               %s  \n' % (i, j, CycleLength(i, j), MagicNumbers(i, j)))
        print('"%i","%i","%i","%s"\n' % (i, j, CycleLength(i, j), MagicNumbers(i, j)))
file.close()
