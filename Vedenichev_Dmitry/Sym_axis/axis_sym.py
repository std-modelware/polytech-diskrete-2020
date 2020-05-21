import itertools


def make_unique(all_possible):  # itertools выдаст нам некоторые повторения, от них избавимся.
    all_different_possible = list()
    for element in all_possible:
        if element not in all_different_possible:
            all_different_possible.append(element)
    return all_different_possible


def make_truly_unique(all_different_possible):
    # Некоторые последовательности выглядит по разному, но если их замкнуть, то они одинаковы
    # С точки зрения поиска симметрии нет смысла рассматривать их отдельно - нашел в одном - в другом идентично
    # Логика проста : Если зацикленная последовательность равна нашей, то она должна войти в ее удвоенную версию
    group = list()
    while all_different_possible:
        word = all_different_possible.pop(0)
        copy = word
        word = list(word)
        # print(word)
        need_to_delete = list()
        for symbol in copy:
            word.append(symbol)
        for elem in all_different_possible:
            str_elem = "".join(str(x) for x in elem)
            str_word = "".join(str(x) for x in word)
            # print(str_word)
            if str_word.find(str_elem) >= 0:
                # print("i delete ", elem)
                # all_different_possible.remove(elem)
                need_to_delete.append(elem)
        group.append(list(copy))
        for elem in need_to_delete:
            all_different_possible.remove(elem)
    # print(all_different_possible)
    return group


def make_var(n, k):
    binary_list = list()
    for i in range(0, n):
        if i > k - 1:
            binary_list.append(0)
        else:
            binary_list.append(1)
    all_possible = itertools.permutations(binary_list)
    all_possible = make_unique(all_possible)  # Избавляемся от повторений
    all_possible = make_truly_unique(all_possible)
    return all_possible


def find_sym(variant):
    sym_axis = 0
    # В случае, если количество вершин нечетно, то ось симметрии обязана проходить через одну из вершин.
    if len(variant) % 2 != 0:
        copy = list(variant)
        for i in range(1, len(variant) + 1):
            # print(copy[0:(len(copy)) // 2 ], ' ', copy[len(copy) // 2 + 1: len(copy)] )
            second_half = list(copy[len(copy) // 2 + 1:len(copy)])
            second_half.reverse()
            if copy[0:(len(copy)) // 2] == second_half:
                sym_axis += 1
                print("Симметрия образована вершиной ", copy[0:len(copy) // 2],
                      copy[len(copy) // 2], copy[len(copy) // 2 + 1:len(copy)])
                break  # Нужно ли?
            symbol = copy.pop(0)
            copy.append(symbol)
    else:  # Симметрия проходит либо через вершины, либо через стороны
        copy = list(variant)

        for i in range(0, len(variant) // 2):
            second_half = list(copy[len(copy) // 2:len(copy)])
            second_half.reverse()
            # print(copy[0:len(copy) // 2], ' ', secondhalf)
            if copy[0:len(copy) // 2] == second_half:  # Если первая  половина равна второй наоборот
                sym_axis += 1
                print("Ось симметрии проходит через стороны так, что разделяет комбинацию на ", copy[0:len(copy) // 2],
                      "и ", copy[len(copy) // 2:len(copy)])

                # second_half.reverse()
            second_half = list(copy[len(copy) // 2 + 1:len(copy)])
            # print(copy[1:len(copy) // 2], ' ', second_half)
            second_half.reverse()
            if copy[1:len(copy) // 2] == second_half:
                sym_axis += 1
                print("Ось симметрии проходит через вершины без скобочек", copy[0], copy[1:len(copy) // 2],
                      copy[len(copy) // 2], copy[len(copy) // 2 + 1:len(copy)])
            symbol = copy.pop(0)
            copy.append(symbol)

    if sym_axis == 0:
        print("Осей симметрии нет")


for i in range(3, 10):
    for j in range(1, i):
        print("Строка длинной ", i, "и ", j, "единицами:")
        variant = make_var(i, j)

        print("Возможные комбинации:")
        print(variant)
        how_many_have_sym = 0
        print("")
        for element in variant:
            print("Для группы вида:", element)
            find_sym(element)
            print("")
        print("")
        print("")
