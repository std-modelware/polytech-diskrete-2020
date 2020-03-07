def kaprekar(number, length, base):
    new_num = convert_from_decimal(number, base).rjust(length, '0')
    list_of_digits = list(new_num)
    list_of_digits.sort(key=lambda ch: int(ch, base))

    minimum = int(''.join(list_of_digits), base)

    list_of_digits.sort(reverse=True)
    maximum = int(''.join(list_of_digits), base)

    return maximum - minimum


def convert_to_decimal(list_of_digits, base):
    return int(list_of_digits, base)


def convert_from_decimal(number, new_base):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < new_base:
        return alphabet[number]
    else:
        return convert_from_decimal(number // new_base, new_base) + alphabet[number % new_base]


def cycle_len(numbers, seek_number):
    length = 0
    for tmp_number in numbers:
        if seek_number == tmp_number:
            return length
        length += 1
    return 0


def find_cycle_or_magic_number(number, base, length, magic_numbers, cycles):
    tmp_number = 0
    used_numbers = []
    while tmp_number is not number and number not in used_numbers:
        tmp_number = number
        used_numbers.append(tmp_number)
        number = kaprekar(tmp_number, length, base)
    if number == tmp_number:
        magic_numbers.add(number)
        return
    if number in used_numbers:
        cycle_length = cycle_len(used_numbers, number)
        for i in range(len(used_numbers) - 1, -1, -1):
            cycles[used_numbers[i]] = cycle_length


def test_len(length, base):
    magic_numbers = set()
    cycles = [0] * 10 ** length
    for number in range(2, base**length):
        find_cycle_or_magic_number(number, base, length, magic_numbers, cycles)
    return magic_numbers, cycles


def test(static_numbers, all_cycles, max_base, max_length):
    for base in range(2, max_base + 1):
        base_magic_nums = []
        base_cycles = []
        for length in range(2, max_length + 1):
            magic_numbers, cycles = test_len(length, base)
            base_cycles.append(cycles)
            base_magic_nums.append(magic_numbers)
        static_numbers.append(base_magic_nums)
        all_cycles.append(base_cycles)


all_magic_nums = []
all_cycles = []
MAX_BASE = 10
MAX_LENGTH = 6
test(all_magic_nums, all_cycles, MAX_BASE, MAX_LENGTH)


file = open('table.csv', 'w')
file.write('"Base","Length","Max length of loop","Magic numbers"\n')

for curLength in range(2, MAX_LENGTH + 1):
    for curBase in range(2, MAX_BASE + 1):
        list_of_magic = []
        for num in all_magic_nums[curBase - 2][curLength - 2]:
            list_of_magic.append(convert_from_decimal(num, curBase))
        file.write('"%i","%i","%i","%s"\n' % (curBase, curLength, max(all_cycles[curBase - 2][curLength - 2]), list_of_magic))
file.close()

