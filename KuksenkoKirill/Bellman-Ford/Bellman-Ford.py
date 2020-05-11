from math import inf


def m_create(sz):
    weight = [[inf] * sz for i in range(0, sz)]
    for i in range(0, sz):
        weight[i][i] = 0
    return weight


def graph_read(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    p = data[0][0]
    q = data[0][1]
    weight = m_create(p)
    graph = {}
    for i in range(1, q + 1):
        v = data[i][0]
        u = data[i][1]
        w = data[i][2]
        if v not in graph:
            graph[v] = {u}
        else:
            graph[v].add(u)
        weight[v][u] = w
    s = data[q + 1][0]
    return graph, p, q, weight, s


def all_edges(graph):
    for v in graph:
        for u in graph[v]:
            yield v, u


def init(s, p):
    predecessor = [-1] * p
    shortest_path = [inf] * p
    shortest_path[s] = 0
    return predecessor, shortest_path


def relax(v1, v2, predecessor, shortest_path, weight):
    if shortest_path[v1] > shortest_path[v2] + weight[v2][v1]:
        shortest_path[v1] = shortest_path[v2] + weight[v2][v1]
        predecessor[v1] = v2


def Bellman_Ford(graph, s, weight, p):
    predecessor, shortest_path = init(s, p)
    for i in range(0, p - 1):
        for v, u in all_edges(graph):
            relax(u, v, predecessor, shortest_path, weight)
    for v, u in all_edges(graph):
        if shortest_path[u] > shortest_path[v] + weight[v][u]:
            return False, False
    return predecessor, shortest_path


def main():
    file = 'test2.txt'

    graph, p, q, weight, s = graph_read(file)

    predecessor, shortest_path = Bellman_Ford(graph, s, weight, p)

    with open('output2.txt', 'w') as f:
        if predecessor is not False:
            print('Вектор предшествования -', predecessor, file=f)
            print('Вектор длин путей -', shortest_path, file=f)
        else:
            print('Граф содержит контур отрицательного веса', file=f)


if __name__ == '__main__':
    main()
