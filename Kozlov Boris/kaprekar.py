def convert_num_from_dec_to_base_r(number, d, r):
    result = ""
    figures = "0123456789ABCDEF"
    while True:
        div, mod = divmod(number, r)
        if div == 0:
            result += figures[mod]
            break
        number = div
        result += figures[mod]
    return ''.join(reversed(result)).rjust(d, '0')


def num_list_to_decimal(number, r):
    result = 0
    multiplier = r ** (len(number) - 1)
    for digit in number:
        result += digit * multiplier
        multiplier /= r
    return result


def kaprekar(r, d, number):
    number_str = str(number).rjust(d, '0')
    number_list = [int(pos, r) for pos in number_str]
    number_list.sort()
    min_number = num_list_to_decimal(number_list, r)
    number_list.reverse()
    max_number = num_list_to_decimal(number_list, r)
    return convert_num_from_dec_to_base_r(int(max_number - min_number), d, r)


def kaprekar_constants(d, r):
    max_number = r ** d
    constants = []
    for dec_number in range(max_number):
        number = convert_num_from_dec_to_base_r(dec_number, d, r)
        num_kaprekar = kaprekar(r, d, number)
        if num_kaprekar == number:
            constants.append(num_kaprekar)
    return constants


def cycle_len(d, r):
    answer = 0
    max_number = r ** d
    for dec_number in range(max_number):
        len = 0
        number = convert_num_from_dec_to_base_r(dec_number, d, r)
        values = [number]
        number = kaprekar(r, d, number)
        while number not in values:
            len += 1
            values.append(number)
            number = kaprekar(r, d, number)
        if len > answer:
            answer = len
    return answer


max_digits_len = 6
max_num_len = 10
file = open('results.csv', 'w')
file.write('"digits","system","maximum number of steps before magic number or cycle appears","magic numbers"\n')
for i in range(1, max_digits_len + 1):
    for j in range(2, max_num_len + 1):
        file.write('"%i","%i","%i","%s"\n' % (i, j, cycle_len(i, j), kaprekar_constants(i, j)))
file.close()
