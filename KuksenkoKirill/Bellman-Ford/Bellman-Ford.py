from math import inf


def m_create(sz):
    weight = [[inf] * sz for i in range(0, sz)]
    for i in range(0, sz):
        weight[i][i] = 0
    return weight


def all_edges(graph, p):
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
        for v, u in all_edges(graph, p):
            relax(u, v, predecessor, shortest_path, weight)
    for v, u in all_edges(graph, p):
        if shortest_path[u] > shortest_path[v] + weight[v][u]:
            return False, False
    return predecessor, shortest_path


def main():
    p, q = [int(x) for x in input('Введите количество узлов и дуг - ').split()]
    graph = {}
    weight = m_create(p)

    print('Вводите начало, конец и вес дуги, нумерация узлов с нуля')
    for i in range(0, q):
        v, u, w = [int(x) for x in input().split()]
        if v >= p or u >= p:
            print('Неверные данные')
            return
        if v not in graph:
            graph[v] = {u}
        else:
            graph[v].add(u)
        weight[v][u] = w

    s = int(input('Введите источник - '))

    predecessor, shortest_path = Bellman_Ford(graph, s, weight, p)

    if predecessor is not False:
        print('Вектор предшествования - ', predecessor)
        print('Вектор длин путей - ', shortest_path)
    else:
        print('Граф содержит контур отрицательного веса')


if __name__ == '__main__':
    main()
