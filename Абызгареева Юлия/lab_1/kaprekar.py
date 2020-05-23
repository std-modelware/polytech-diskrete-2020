from threading import Thread


def convertFromDec(number, base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < base:
        return alphabet[number]
    else:
        return convertFromDec(number // base, base) + alphabet[number % base]


def convertToDec(list_number, base):
    return int(''.join(list_number), base)


def kaprekar(number_ten, n, base):
    number = convertFromDec(number_ten, base).rjust(n, '0')
    number_list = list(str(number))
    number_list.sort(reverse=True)
    direct = int(''.join(number_list), base)
    number_list.sort()
    invert = int(''.join(number_list), base)
    return direct - invert


def get_min(base, n):
    return base ** (n - 1)


def get_max(base, n):
    result = 0
    for k in range(1, n):
        result += (base - 1) * (base ** k)
    result += base - 2
    return result


def research_step(base, n, number_ten):
    history = []
    new_number = number_ten
    while new_number not in history:
        history.append(new_number)
        new_number = kaprekar(history[len(history) - 1], n, base)
    return len(history) - history.index(new_number)


def research(iBase, iN):
    fixed_points = []
    max_len_of_cycle = -1
    right_border = get_max(iBase, iN)
    left_border = 1
    for number in range(left_border, right_border + 1):
        cycle_len = research_step(iBase, iN, number)
        if cycle_len > max_len_of_cycle:
            max_len_of_cycle = cycle_len
        if number not in fixed_points and number == kaprekar(number, iN, iBase):
            fixed_points.append(convertFromDec(number, iBase).rjust(iN, '0'))
    return {"Max len of loop": max_len_of_cycle - 1, "Fixed points": fixed_points}

def general_research(max_base, max_n):
    general_result = [[]]
    general_result[0].append("---")
    for iN in range(2, max_n + 1):
        general_result[0].append("Length = %i" % iN)
    for iBase in range(2, max_base + 1):
        general_result.append(["Base: %i" % iBase])
        for iN in range(2, max_n + 1):
            result = research(iBase, iN)
            general_result[iBase - 1].append(result)
    return general_result


def dump_research(result, filename):
    file = open(filename, "w")
    for row in result:
        for column in row:
            data = str(column)
            if isinstance(column, dict):
                data = data.replace(",", ";")
            file.write(data)
            file.write(',')
        file.write('\n')


res = general_research(10, 6)
dump_research(res, "research.csv")
