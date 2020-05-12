def convert_from_decimal(number: int, base: int):
    if number == 0:
        return '0'
    
    vocab = ('A', 'B', 'C', 'D', 'E', 'F')
    result = []
    i = 0
    while number > 0:
        tmp = number % base
        result.append(tmp)
        number = number // base
        if result[i] >= 10:
            j = 0
            while result[i] != j + 10:
                j += 1
            result[i] = vocab[j]
        i += 1
    result.reverse()
    result: str = "".join(map(str, result))
    return result

def convert_to_decimal(number: str, base: int):
    return int(number, base)

def fulfill_number(number: str, length: int):
    return '0' * (length - len(number)) + number

def kaprekar(number: str, base: int):
    number_list = list(number)
    minimum = int(''.join(sorted(number_list)), base)
    maximum = int(''.join(sorted(number_list, reverse=True)), base)
    return maximum - minimum

def is_magic(number: str, base: int, length: int):
    for cycle_len in range(1, 10):
        if number == fulfill_number(convert_from_decimal(kaprekar(number, base), base), length):
            return cycle_len, number
        else:
            number = fulfill_number(convert_from_decimal(kaprekar(number, base), base), length)
    if (cycle_len == 9):
        return 0, 0

used_magic_numbers = []
MAX_LENGTH = 6
MAX_BASE = 16

file = open("results.txt", "w")

for base in range(2, MAX_BASE + 1):
    for length in range(1, MAX_LENGTH + 1):
        file.write("base: {0}\tlength: {1}\n".format(base, length))
        print("base: {0}\tlength: {1}\n".format(base, length))
        for number in range(base ** length):
            number = convert_from_decimal(number, base)
            number = fulfill_number(number, length)
            cycle_len, magic_number = is_magic(number, base, length)
            if cycle_len != 0 and (magic_number, base) not in used_magic_numbers:
                file.write("'{0}': {1}, ".format(magic_number, cycle_len))
                used_magic_numbers.append((magic_number, base))
        file.write("\n\n")

file.close()