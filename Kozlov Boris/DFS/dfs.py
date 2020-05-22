"""
В программу из файла передается ориентированный
граф, записанный в виде списка дуг. Строки вида "a b"
в данном случае означают направление b->a. Первая строка
файла содержит количество вершин орграфа. Задача: провести
топологическую сортировку введенного орграфа, используя
поиск в глубину. Если сортировка невозможна, вернуть [].
"""


class Solution(object):
    def __init__(self, num_courses, prerequisites):
        self.numC = num_courses
        self.visited = [False for i in range(num_courses)]
        self.visiting = [False for i in range(num_courses)]
        self.res = []
        self.graph = [[] for i in range(num_courses)]
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])

    def __dfs(self, node):
        if self.visiting[node] is True:
            return True
        if self.visited[node] is True:
            return False
        self.visiting[node] = True
        for j in self.graph[node]:
            if self.__dfs(j) is True:
                return True
        self.visiting[node] = False
        self.visited[node] = True
        self.res.append(node)
        return False

    def find_order(self):
        for i in range(self.numC):
            if self.__dfs(i) is True:
                return []
        return self.res


def read_graph(source):
    file = open(source)
    dim = int(file.readline())
    edge_list = []
    for line in file:
        edge = [int(vertex) for vertex in line.split()]
        edge_list.append(edge)
    return dim, edge_list


# ациклический орграф можно упорядочить
num_c, graph = read_graph("Test.txt")
sol = Solution(num_c, graph)
print(sol.find_order())
# зациклим его
num_c, graph = read_graph("Test2.txt")
sol = Solution(num_c, graph)
print(sol.find_order())
