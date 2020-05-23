import random


def number_to_digits(number, quantity, radix):
    digits_array = []
    for i in range(quantity):
        number, digit = divmod(number, radix)
        digits_array.append(digit)
    digits_array.reverse()
    return digits_array


def digits_to_number(digits, radix):
    mul = 1
    res = 0
    for i in range(len(digits) - 1, -1, -1):
        res += digits[i] * mul
        mul *= radix
    return res


def array_subtraction(digits_arr1, digits_arr2, radix):
    res = [0 for i in range(len(digits_arr1))]
    for i in range(len(digits_arr1) - 1, -1, -1):
        res[i] = digits_arr1[i] - digits_arr2[i]
        if res[i] < 0:
            digits_arr1[i - 1] -= 1
            res[i] += radix
    return res


def kaprekar_internal(digits_arr, radix):
    digits_arr.sort()
    digits_arr_big = digits_arr.copy()
    digits_arr_big.sort(reverse=True)
    return array_subtraction(digits_arr_big, digits_arr, radix)


def kaprekar(number, digits, radix):
    return digits_to_number(kaprekar_internal(number_to_digits(number, digits, radix), radix), radix)


def next_possible_number(digits_arr, radix):
    for i in range(len(digits_arr) - 1, -1, -1):
        if digits_arr[i] < (radix - 1):
            digits_arr[i] += 1
            for j in range(i + 1, len(digits_arr), 1):
                digits_arr[j] = digits_arr[i]
            return digits_arr
    return []


def multiset_compare(digits_arr1, digits_arr2):
    buf = digits_arr2.copy()
    for d1 in digits_arr1:
        found = False
        for d2 in buf:
            if d1 == d2:
                buf.remove(d2)
                found = True
                break
        if not found:
            return False
    return True


def fixed_numbers(digits, radix):
    magic_nums = []
    num = [0 for i in range(digits)]
    while len(num):
        res = kaprekar_internal(num, radix)
        if multiset_compare(res, num):
            magic_nums.append(res)
        num = next_possible_number(num, radix)
    return magic_nums


def find_cycles(digits, radix, magic_numbers):
    cycle_arr = []
    number = [0 for i in range(digits)]
    while len(number):
        cycle = []
        if number not in magic_numbers:
            cycle.append(number)
            res = kaprekar_internal(number, radix)
            while res not in magic_numbers and res not in cycle:
                cycle.append(res.copy())
                res = kaprekar_internal(res, radix)
            if res not in magic_numbers:
                visited = False
                for c in cycle_arr:
                    if res in c:
                        visited = True
                        break
                if not visited:
                    while cycle[0] != res:
                        cycle.remove(cycle[0])
                    cycle_arr.append(cycle)
        number = next_possible_number(number, radix)
    return cycle_arr


def max_depth(digits, radix, magic_numbers, cycles):
    max_d = 0
    num = [0 for i in range(digits)]
    while len(num):
        local_max_d = 0
        num1 = num
        while num1 not in magic_numbers:
            cycle_reached = False
            for cycle in cycles:
                if num1 in cycle:
                    cycle_reached = True
                    break
            if not cycle_reached:
                num1 = kaprekar_internal(num1, radix)
                local_max_d += 1
            else:
                break
        max_d = max(max_d, local_max_d)
        num = next_possible_number(num, radix)
    return max_d


for i in range(2, 11):
    for j in range(2, 11):
        print(i, ' ', j, ':', end=' ')
        numbers = fixed_numbers(i, j)
        print("[", end=' ')
        for n in numbers:
            print("".join(map(str, n)), end=' ')
        print("]", end='; ')
        cyc = find_cycles(i, j, numbers)
        print(len(cyc), end='; ')
        max_len = 0
        for c in cyc:
            max_len = max(max_len, len(c))
        print(max_len, end='; ')
        print(max_depth(i, j, numbers, cyc))
