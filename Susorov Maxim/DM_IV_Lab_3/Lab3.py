import copy


def FindCycle(edges: list, vertex_count: int):
    """
    Functions response a question: does graph has cycle?
    :param edges: list of edges in graph
    :param vertex_count: count of edges in graph
    :return: bool()
    """
    def DFS_proc(_edges: list, _colors: list, _current_vertex: int, _prev_vertex: int, _cycle_found: list):
        """
        Recursive function of depth-first search. Function stops when it finds cycle
        :param _edges: list of edges in graph
        :param _colors: list of colored vertices. 0 - white (not touched), 1 - grey (in progress), 2 - black (done)
        :param _current_vertex: current vertex
        :param _prev_vertex: previous vertex (it is needed to find cycle)
        :param _cycle_found: list(bool()) - analogue of pointer to variable 'cycle_found' in outer function
        :return: none
        """
        _colors[_current_vertex] = 1
        for e in _edges:
            if e[0] == _current_vertex:
                if _colors[e[1]] == 0:
                    DFS_proc(edges, _colors, e[1], _current_vertex, _cycle_found)
                elif _colors[e[1]] == 1 and e[1] != _prev_vertex:
                    _cycle_found[0] = True
                    return None
            if e[1] == _current_vertex:
                if _colors[e[0]] == 0:
                    DFS_proc(edges, _colors, e[0], _current_vertex, _cycle_found)
                elif _colors[e[0]] == 1 and e[0] != _prev_vertex:
                    _cycle_found[0] = True
                    return None
        _colors[_current_vertex] = 2

    cycle_found = [False]
    colors = [0] * vertex_count
    for vertex in range(vertex_count):
        if colors[vertex] == 0 and not cycle_found[0]:
            DFS_proc(edges, colors, vertex, -1, cycle_found)
    return cycle_found[0]


def KruskalAlgorithm(_edges: list, vertex_count: int):
    """
    Functions finds MST of the graph
    :param _edges: list of edges in graph
    :param vertex_count: count of vertices in graph
    :return: list of edges in MST
    """
    edges = sorted(_edges, key=lambda edge: edge[2])
    MST = list()
    k = 0
    for i in range(vertex_count):
        while k < len(edges) - 1:
            z = copy.deepcopy(MST)
            z.append(edges[k])
            if FindCycle(z, vertex_count):
                k += 1
            else:
                break
        if k >= len(edges) - 1:
            break
        MST.append(edges[k])
        k += 1
    return MST


edges = [
    [0, 4, 1],
    [0, 1, 3],
    [1, 4, 4],
    [1, 2, 5],
    [2, 4, 6],
    [2, 3, 2],
    [3, 4, 7]
]
vertex_count = 5
print(KruskalAlgorithm(edges, vertex_count))
