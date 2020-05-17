class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = int(x)
        self._y = int(y)

    def __init__(self, array: list) -> None:
        self._x = int(array[0])
        self._y = int(array[1])

    def get_coord(self) -> tuple:
        return self._x, self._y

    def distance_to_point(self, p: 'Point') -> int:
        return abs(self._x - p._x) + abs(self._y - p._y)

    @staticmethod
    def distance(p1: 'Point', p2: 'Point') -> int:
        return abs(p1._x - p2._x) + abs(p1._y - p2._y)


# создание полной матрицы смежности, где вес ребра это расстояние между вершинами
def create_adjacency_matrix(count: int, data: 'list[Point]') -> 'list[list[int]]':
    return [[Point.distance(data[i], data[j]) for j in range(count)] for i in range(count)]


# получение данных из файла
def get_data():
    with open('in.txt', 'r') as file:
        count = int(next(file))
        return count, [Point(line[:-1].split(' ')) for line in file]


# алгоритм Ярника-Прима-Дейкстры
def YPD(count: int, adj_mat: 'list[list[Point]]') -> 'tuple(list(list(int)), int)':
    weight = 0  # инициализируем вес рёбер остова
    unused_vertexes = set(i for i in range(count))  # непосещённые вершины
    minimum_spanning_tree = []  # инициализируем множество вершин остова
    start_vertex = 0  # выбираем первую вершину
    unused_vertexes.remove(start_vertex)  # удаляем её из множества непосещённых вершин
    minimum_spanning_tree.append(start_vertex)
    while unused_vertexes:  # проверка множества на пустоту
        min_weight = 99999999999
        min_edge = None
        # проходим по вершинам minimum_spanning_tree
        for mst_vertex in minimum_spanning_tree:
            # выбор непосещённого ребра с минимальным весом, лежащим между minimum_spanning_tree и unused_vertexes
            for v in unused_vertexes:
                if (adj_mat[mst_vertex][v] > 0) and (adj_mat[mst_vertex][v] < min_weight):
                    min_weight = adj_mat[mst_vertex][v]
                    min_edge = (mst_vertex, v)
        adj_mat[min_edge[0]][min_edge[1]] = -1  # метим ребро
        adj_mat[min_edge[1]][min_edge[0]] = -1  # метим ребро
        weight += min_weight  # добавляем вес ребра к весу всего остова
        minimum_spanning_tree.append(min_edge[1])  # добавляем вершину к остову (в конец)
        unused_vertexes.remove(min_edge[1])  # удаляем вершину из непосещённых
    return adj_mat, weight


# вывод результата
def write_result(adj_mat, weight):
    with open('out.txt', 'w') as file:
        for lst in adj_mat:
            for j in range(len(lst)):
                if lst[j] == -1:
                    file.write(str(j + 1) + ' ')
            file.write('0\n')
        file.write(str(weight))


def main():
    count, points = get_data()
    adj_matrix = create_adjacency_matrix(count, points)
    adj_mat, weight = YPD(count, adj_matrix)
    write_result(adj_mat, weight)


if __name__ == '__main__':
    main()
