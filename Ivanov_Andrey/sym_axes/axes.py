import itertools

# Получаем все возможные комбинации длины n с m единицами
def get_all_combinations(n, m):
    binary_range = list()
    unique = list()
    for i in range(0, n):
        if i > m - 1:
            binary_range.append(0)
        else:
            binary_range.append(1)
    permutation = itertools.permutations(binary_range)
    # Учитываем только неповторяющиеся
    for perm_unit in permutation:
        if perm_unit not in unique:
            unique.append(perm_unit)
    return unique

# Создание класса эквивалентности по списку
def get_all_equivalent(arr):
    eq_arr = list()
    new_arr = list()
    for i in range(0, len(arr) - 1):
        if i == 0:
            new_arr = list(arr).copy()
        tmp = new_arr[0]
        new_arr.remove(tmp)
        new_arr.append(tmp)
        eq_arr.append(new_arr.copy())
    return eq_arr

# Ищем разные классы эквивалентности
def get_not_equivalent(unique_arr):
    eq_arr = list()
    non_eq_arr = list()
    for arr in unique_arr:
        arr = list(arr)
        if arr not in eq_arr:
            non_eq_arr.append(tuple(arr))
            eq_arr.extend(get_all_equivalent(arr).copy())
    return non_eq_arr

# Ищем оси симметрии
def get_sym_axis(non_eq_arr):
    axis_count = 0
    eq_arr = get_all_equivalent(non_eq_arr);
    if len(non_eq_arr) % 2 == 1:
        for arr in eq_arr:
            tmp = arr.copy()
            tmp.reverse()
            if tmp == arr:
                non_eq_arr = tmp.copy()
                print("\t", non_eq_arr, "-", end=' ')
                print("Ось симметрии - прямая, проходящая через среднюю точку ", arr[len(arr) // 2])
                axis_count += 1
    else:
        step_count = len(non_eq_arr) / 2  # если четное кол-во вершин, достаточно пройти половину из них
        for arr in eq_arr:
            step_count -= 1
            tmp = arr.copy()
            tmp.reverse()
            if tmp == arr:
                non_eq_arr = tmp.copy()
                print("\t\t", non_eq_arr, "-", end=' ')
                print("Ось симметрии - прямая, проходящая между ", arr[len(arr) // 2 - 1], "и",
                      arr[len(arr) // 2])  # проходит через сторону, по обеим сторонам которой данные точки
                axis_count += 1
            tmp = arr.copy()
            vec_end = tmp.pop(len(tmp) - 1)
            tmp_arr = tmp.copy()
            tmp.reverse()
            if tmp == tmp_arr:
                tmp.append(vec_end)
                non_eq_arr = tmp.copy()
                print("\t\t", non_eq_arr, "-", end=' ')
                print("Ось симметрии - прямая, проходящая через точки ", arr[len(tmp) // 2 - 1], "и",
                      arr[len(tmp) - 1])  # "разрезает напополам" данный правильный многоугольник
                axis_count += 1
            if step_count == 0:
                break
    if axis_count == 0:
        print("\t\tОси симметрии отсутствуют")
    return axis_count

n, m = input("Введите длину строки и количество единиц:\n").split()
n = int(n)
m = int(m)
combinations = list(get_all_combinations(n, m))
non_eq_combinations = (get_not_equivalent(combinations))
print("Все возможные комбинации:")
for comb in combinations:
    print("\t", comb)
print("Классы эквивалентности:")
for non_eq_comb in non_eq_combinations:
    print("\t", non_eq_comb)
print("Оси симметрии:")
for non_eq_comb in non_eq_combinations:
    print("\tДля", non_eq_comb, ":")
    get_sym_axis(non_eq_comb)
