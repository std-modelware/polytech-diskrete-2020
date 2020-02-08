def kaprekar(number, d):
    number_str = str(number)
    while len(number_str) < d:
        number_str = '0' + number_str
    list_from_number = [int(ch) for ch in number_str]
    list_from_number.sort()
    min_num = int("".join(str(ch) for ch in list_from_number))
    list_from_number.reverse()
    max_num = int("".join(str(ch) for ch in list_from_number))
    return max_num - min_num

def findMagicNumbers(d):
    max_number = 10 ** d
    magic_numbers = []
    for i in range(max_number):
        if i == kaprekar(i, d):
            magic_numbers.append(i)
    return magic_numbers


print(findMagicNumbers(4))


