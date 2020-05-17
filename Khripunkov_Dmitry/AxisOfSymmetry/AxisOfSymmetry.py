import itertools

def str_to_list(s: str):
    l = [i for i in s]
    return l

def list_to_str(l: list):
    s = ''.join(l)
    return s

def cycle(l: list, n: int):
    res = list()
    count = 0
    for i in l:
        number = str_to_list(i)
        check = str_to_list(i)
        count = 0
        while count < n - 1:
            number.append(number.pop(0))
            if number == check:
                break
            if list_to_str(number) in l:
                l.remove(list_to_str(number))
            count += 1
    return l

def list_shift(l: list):
        l.insert(0, l.pop())
        return l

def all_combinations(n: int, k: int):
    tmp = list()
    l = list()
    l = '1' * k + '0' * (n - k)
    for i in itertools.permutations(l, n):
        num = ''.join(i)
        if num not in tmp:
            tmp.append(num)
    res = cycle(tmp, n)
    return res

def check(l: list):
    for i in range(0, len(l) // 2):
        if l[i] != l[-1- i]:
            return False
    return True

def check2(l: list):
    length = len(l)
    for i in range(1, length // 2):
        if l[i] != l[-i]:
            return False
    return True

def axis(number: list):
    length = len(number)
    if (length % 2) == 0:
        if check(number) == True:
            print(list_to_str(number[0 : len(number) // 2]), '  |  ', list_to_str(number[len(number) // 2 : ]));
            return True
        elif check2(number) == True:
            print('(', number[0], ')', list_to_str(number[1 : length // 2]), '(', number[length // 2], ')', \
                  list_to_str(number[length // 2 + 1 : length]))
            return True
    else:
        number = list_to_str(number)
        tmp1 = number.pop(0)
        if check(number) == True:
            number.insert(0, tmp1)
            print('(', number[0], ')', list_to_str(number[1 : l]))
            return True
    return False

def symmetry(n: int, k: int):
    combs_list = all_combinations(n, k)
    for number in combs_list:
        print(number)
        axis_number = 0
        count = 0
        while count < n:
            tmp = axis(number)
            number = list_shift(str_to_list(number))
            if tmp == True:
                axis_number += 1
            count += 1
        print('Number of axis: ', axis_number)

n = int(input('Input number length: '))
k = int(input('Input amount of ones: '))
symmetry(n, k)