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

# Выделяем элемент, через который проходит ось симметрии
def mark(elem):
    return "[" + str(elem) + "]"

def list2str(_list):
    _str = ""
    for elem in _list:
        _str += str(elem)
    return _str

# Ищем оси симметрии
# Изменение вывода: если ось проходит через какую-либо вершину, вершина отображается в квадратных скобках "[ ]"
# Например: 0[1]2- ось проходит только через вершину 1, 0[1]2[3] - ось проходит через две вершины - 1 и 2
# Если ось есть и при этом не проходит через вершины, то сторона, которую эта ось пересекает, обозначается прямой чертой "|"
# Например: 12|34 - ось проходит через сторону, которая соединяет вершины 3 и 4
def get_sym_axis(non_eq_arr):
    axis_count = 0
    eq_arr = get_all_equivalent(non_eq_arr);
    if len(non_eq_arr) % 2 == 1:
        for arr in eq_arr:
            tmp = arr.copy()
            tmp.reverse()
            if tmp == arr:
                non_eq_arr = tmp.copy()
                non_eq_arr[len(arr) // 2] = mark(arr[len(arr) // 2])
                print("\t", list2str(non_eq_arr), "-", end=' ')
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
                non_eq_arr.insert(len(arr) // 2, "|")
                print("\t\t", list2str(non_eq_arr), "-", end=' ')
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
                non_eq_arr[len(tmp) // 2 - 1] = mark(arr[len(tmp) // 2 - 1])
                non_eq_arr[len(tmp) - 1] = mark(arr[len(tmp) - 1])
                print("\t\t", list2str(non_eq_arr), "-", end=' ')
                print("Ось симметрии - прямая, проходящая через точки ", arr[len(tmp) // 2 - 1], "и",
                      arr[len(tmp) - 1])  # "разрезает напополам" данный правильный многоугольник
                axis_count += 1
            if step_count == 0:
                break
    if axis_count == 0:
        print("\t\tОси симметрии отсутствуют")
    return axis_count

for n in range(3, 10):
    for m in range(1, n):
        print("\nДлина строки", n, "с количеством единиц", m, ":")
        combinations = list(get_all_combinations(n, m))
        non_eq_combinations = (get_not_equivalent(combinations))
        # print("Все возможные комбинации:")
        # for comb in combinations:
        #     print("\t", comb)
        print("Классы эквивалентности:")
        for non_eq_comb in non_eq_combinations:
            print("\t", non_eq_comb)
        print("Оси симметрии:")
        for non_eq_comb in non_eq_combinations:
            print("\tДля", non_eq_comb, ":")
            get_sym_axis(non_eq_comb)
