# Провекра графа на существование эйлерова цикла
def check_if_cycle(graph):
    null_count = 0
    for top in graph:
        if len(top) == 0:
            null_count += 1
        elif len(top) % 2 == 1:
            return False
    if null_count == len(graph):
        return False
    return True


# Пробегаем по графу и получаем цикл
def get_euler_cycle(graph, top):
    stack = list()
    cycle = list()
    v = top
    stack.append(v)
    while len(stack) > 0:
        deg = len(graph[v])
        if deg == 0:
            cycle.append(v)
            tmp_ind = stack.pop()
            if len(stack) > 0:
                v = stack[len(stack) - 1]
        else:
            tmp = graph[v].pop(0)
            graph[tmp].remove(v)
            stack.append(tmp)
            v = tmp
    return cycle


# Форматирование вывода
def list2str(_list):
    _str = ""
    for elem in _list:
        _str += str(elem)
        _str += "->"
    _str = _str[:len(_str) - 2]
    return _str


# Преобразование введенных данных
def str2list(_str):
    _list = list()
    for elem in _str:
        elem = int(elem)
        _list.append(elem)
    return _list


# Тестовый граф
# test_graph = (
#     [1, 4],  # 0
#     [0, 5, 2, 3],  # 1
#     [1, 5, 3, 4],  # 2
#     [4, 5, 2, 1],  # 3
#     [0, 5, 2, 3],  # 4
#     [1, 2, 3, 4]  # 5
# )


# Интерактивный блок
graph = list()
n = input("Введите количество вершин графа: ")
n = int(n)
graph_top = tuple(range(n))
print("Нумерация вершин:", graph_top)
for top in graph_top:
    print("Укажите через пробел вершины, смежные с вершиной", top, end=": ")
    tmp = input().split()
    tmp = str2list(tmp)
    graph.append(tmp)
test_graph = graph.copy()
graph = tuple(graph)
print("Введен граф, заданный списком смежности:", graph)
if not check_if_cycle(test_graph):
    print("Эйлеров цикл в данном графе отсутствует")
else:
    print("Эйлеров цикл в данном графе существует")
    start_pos = input("Укажите вершину, с которой хотите начать: ")
    start_pos = int(start_pos)
    if start_pos in graph_top:
        print("Маршрут:", list2str(get_euler_cycle(test_graph, start_pos)))
    else:
        print("Такая вершина в графе отсутсвует")
