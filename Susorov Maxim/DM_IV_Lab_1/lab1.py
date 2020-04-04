from threading import Thread


def convert_from_decimal(number, base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < base:
        return alphabet[number]
    else:
        return convert_from_decimal(number // base, base) + alphabet[number % base]


def convert_to_decimal(list_number, base):
    return int(''.join(list_number), base)


def kaprekar(number10, n, base):
    number = convert_from_decimal(number10, base).rjust(n, '0')
    number_list = list(str(number))
    number_list.sort(reverse=True)
    direct = int(''.join(number_list), base)
    number_list.sort()
    invert = int(''.join(number_list), base)
    return direct - invert


def get_minimal_argument_in_current_base(base, n):
    return base ** (n - 1)


def get_maximal_argument_in_current_base(base, n):
    result = 0
    for k in range(1, n):
        result += (base - 1) * (base ** k)
    result += base - 2
    return result


def research_step(base, n, number10):
    history = []
    new_number = number10
    while new_number not in history:
        history.append(new_number)
        new_number = kaprekar(history[len(history) - 1], n, base)
    return len(history) - history.index(new_number)


def research(iBase, iN):
    fixed_points = []
    maximal_length_of_cycle = -1
    left_border = get_minimal_argument_in_current_base(iBase, iN)
    right_border = get_maximal_argument_in_current_base(iBase, iN)
    for number in range(left_border, right_border + 1):
        cycle_length = research_step(iBase, iN, number)
        if cycle_length > maximal_length_of_cycle:
            maximal_length_of_cycle = cycle_length
        if number not in fixed_points and number == kaprekar(number, iN, iBase):
            fixed_points.append(convert_from_decimal(number, iBase))
    return {"Max len of loop": maximal_length_of_cycle - 1, "List of fixed points": fixed_points}


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


res = general_research(16, 6)
dump_research(res, "research.csv")
