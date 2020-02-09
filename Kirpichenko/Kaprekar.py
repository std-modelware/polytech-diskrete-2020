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
    min_num = dec(list_from_number, r) # int("".join(str(ch) for ch in list_from_number))
    list_from_number.reverse()
    max_num = dec(list_from_number, r) # int("".join(str(ch) for ch in list_from_number))
    return convTo(max_num - min_num, r)


def findMagicNumbers(d, r):
    max_number = r ** d
    magic_numbers = []
    for i in range(max_number):
        tmp = kaprekar(convTo(i, r), d, r)
        if i == int(tmp, r):
            magic_numbers.append(tmp)
    return magic_numbers


print(findMagicNumbers(3, 16))
