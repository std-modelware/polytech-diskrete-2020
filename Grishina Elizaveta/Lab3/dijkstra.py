from _collections import deque
import math


def read_graph(file, num_v):
    """
    :param file: str - filename
    :param num_v: int - number of vertexes
    :return: list(list(num)) - adjacency matrix
    """
    fp = open(file, 'r')
    tmp = list()
    matrix = list()
    for i in range(num_v):
        tmp.append(fp.readline().strip())
    for string in tmp:
        matrix.append(str_num(string))
    return matrix


def str_num(string):
    """
    :param string: str - string of numbers
    :return: list(int) - list of numbers
    """
    num = list()
    for elem in string:
        if elem == ' ':
            continue
        else:
            num.append(int(elem))
    return num


def dijkstra(matrix, start):
    """
    :param matrix: list(list(int)) - adjacency matrix
    :param start: int - start vertex
    :return: prev - list(int) - list of previous vertexes in the shortest path
    :return: dist - list(int) - list of distances from start to each vertex
    """
    q = deque()
    size = len(matrix)
    dist = [math.inf]*size
    dist[start - 1] = 0
    used = [False]*size
    p = [-1]*size
    q.append(start)
    prev = [None]*size
    while len(q) != 0:
        tmp = q.popleft()
        for i in range(size):
            weight = matrix[tmp-1][i]
            if weight != 0:
                if dist[tmp-1] + weight < dist[i]:
                    dist[i] = dist[tmp-1] + weight
                    prev[i] = tmp
                    if used[i] is False:
                        q.append(i+1)
                        used[i] = True
    return prev, dist


def build_path(start, prev, fin):
    """
    :param start: int - start vertex
    :param prev: list(int) - list of previous vertexes in the shortest path
    :param fin: int - destination vertex
    :return: list(int) - list of vertexes in the shortest path
    """
    if start == fin:
        return 0
    path = list()
    path.append(fin)
    while prev[fin - 1] is not None:
        path.append(prev[fin - 1])
        fin = prev[fin - 1]
    path.reverse()
    return path


def print_shortest_paths(file, matrix, start):
    """
    :param file: str - file name
    :param matrix: list(list(int))
    :param start: int - start vertex
    :return: nothing
    """
    fp = open(file, 'w')
    prev, dist = dijkstra(matrix, start)
    for i in range(len(prev)+1):
        if i == start or i == 0:
            continue
        path = build_path(start, prev, i)
        fp.write('The shortest path from ' + str(start) + ' to ' + str(i) + str(path) + ' the length is ' + str(dist[i-1]) + '\n')
    fp.close()


print_shortest_paths('output.txt', read_graph("input.txt", 7), 5)
