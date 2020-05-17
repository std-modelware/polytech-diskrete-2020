def generate_adjency_matrix():
    with open('in.txt', 'r') as file:
        next(file)
        adj_mat = [list(map(lambda x: -1*int(x), s.split())) for s in file]
    return adj_mat


def write_result(res):
    with open('out.txt', 'w') as file:
        file.write(str(res))


# вычитаение минимума из каждого столбца и строки
def sub_min_from_each_row_and_col(mat):
    gen_mat = []
    r_n = range(len(mat))
    for i in r_n:
        min_e = min(mat[i])
        gen_mat.append([e - min_e for e in mat[i]])
    for i in r_n:
        min_e = min([gen_mat[j][i] for j in r_n])
        for j in r_n:
            gen_mat[j][i] -= min_e
    return gen_mat


def kuhn(adj_list, x):
    if used[x]:
        return False
    used[x] = True
    for y in adj_list[x]:
        if (mt_chain[y] == -1) or (kuhn(adj_list, mt_chain[y])):
            mt_chain[y] = x
            return True
    return False


def hungarian_algorithm(adj_mat):
    r_n = range(len(adj_mat))

    # получаем нули в матрице mat
    # таким образом мы "метим" интересные нам значения, чтобы попытаться построить полное паросочетание
    mat = sub_min_from_each_row_and_col(adj_mat)

    # для простоты кода
    global used
    global mt_chain

    while True:
        # подготовка списка смежности, и применение алгоритма Куна для поиска полного паросочетания
        adj_list = [[j for j in r_n if mat[i][j] == 0] for i in r_n]
        mt_chain = [-1 for i in r_n]
        for i in r_n:
            used = [False for i in r_n]
            kuhn(adj_list, i)

        # условие выхода
        if -1 not in mt_chain:
            return mt_chain

        x_set = set(i for i in r_n if i not in mt_chain)
        x_delta = set()  # вершины(строки), из которых будем вычитать delta
        y_delta = set()  # вершины(столбцы), к которым прибавим delta

        # поиск x и y вершин, в которые можно попасть из x, который не попал в mt-цепь
        for x in x_set:
            for y in adj_list[x]:
                if mt_chain[y] != -1:
                    y_delta.add(y)
                    x_delta.add(mt_chain[y])
        x_delta.update(x_set)

        # выбор минимального значения delta из доступных элементов матрицы
        selected_e = []
        for i in x_delta:
            for j in set(r_n).difference(y_delta):
                selected_e.append(mat[i][j])
        delta = min(selected_e)

        # пересчитывание матрицы с учётом delta
        for i in y_delta:
            for h in r_n:
                mat[h][i] += delta
        for i in x_delta:
            for j in r_n:
                mat[i][j] -= delta


def main():
    # матрица загружается в отрицательных числах, чтобы решать задачу поиска минимума
    adj_mat = generate_adjency_matrix()
    chain = hungarian_algorithm(adj_mat)
    s = 0
    for i in range(len(adj_mat)):
        s += adj_mat[chain[i]][i]

    # домножаем на -1, так как искали минимум в отрицательных числах, и получили максимум в положительных
    write_result(-1*s)


if __name__ == '__main__':
    main()
