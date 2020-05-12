# Найти количество компонент связности неориентированного графа при помощи поиска в глубину.
# Формат входных данных:
# Пишите в файле пожалуйста.
# На вход подаётся описание графа.
# В первой строке указаны два натуральных числа, разделенные пробелом, количетво вершин v и количество ребер e
# В следующих e строках содержатся описания рёбер.
# Каждое ребро задаётся разделённой пробелом парой номеров вершин, которые это ребро соединяет.
# Считается, что вершины графа пронумерованы числами от 1 до v.
# Формат выходных данных:
# Одно число — количество компонент связности графа.

# пример 1:
# 4 2
# 1 2
# 3 2
# Выход 2

# пример 2:
# 4 3
# 1 2
# 3 2
# 4 3
# Выход 1

# пример 3
# 7 7
# 1 2
# 1 6
# 2 4
# 2 6
# 4 6
# 1 4
# 5 7
# Выход 3

f = open('C:/Users/shaoj/PycharmProjects/Graph/Primer_input.txt', 'r')

# Вход : количетво вершин v и количество ребер e
# Выход : матрица смежности
def Init(v: int, e: int):
    Graph: list = [[0]*v for i in range(v)]
    i: int
    j: int

    for i in range (0,e,1):
        p = f.read(1)
        while (p == "\n" or p == " "):
            p = f.read(1)
        p = int(p)

        q = f.read(1)
        while (q == "\n" or q == " "):
            q = f.read(1)
        q = int(q)
        Graph[p - 1][q - 1] = 1
        Graph[q - 1][p - 1] = 1

    return Graph

# Вход : матрица смежности Graph, проиденные вершины visited, количетво вершин v и вход entrance
# Выход : нет
# В функции все возможные вершины, от которой можно найти один путь к entrance, будут отмечаться на 1.
# visited[i] = 1 -- она уже отмечана
# visited[i] = 0 -- она еще не отмечана

# С помощью структуры стека
def DFS(Graph: list, visited: list, v: int, entrance: int):
    i: int = 0
    stack: list = []
    stack.append(entrance)
    visited[entrance] = 1
    while(len(stack) > 0):
        vertex = stack.pop(len(stack) - 1)
        for i in range(0,v,1):
            if(Graph[vertex][i] == 1 and visited[i] == 0):
                visited[i] = 1
                stack.append(i)

# тоже можно с помощью рекурсий
def DFS_Recurtion(Graph: list, visited: list, v: int, entrance: int):
    i: int = 0
    for i in range(0,v,1):
        if(Graph[entrance][i] == 1 and visited[i] == 0):
            visited[i] = 1
            DFS_Recurtion(Graph, visited, v, i)

def MAIN():
    v = f.read(1)
    while (v == "\n" or v == " "):
        v = f.read(1)
    v = int(v)

    e = f.read(1)
    while (e == "\n" or e == " "):
        e = f.read(1)
    e = int(e)

    n: int = 0
    i: int = 0
    Graph = Init(v,e)
    visited = [0] * v

    print("Stack:")
    for i in range (0,v,1):
        if(visited[i] == 0):
            DFS(Graph, visited, v, i)
            n = n + 1
    print(n)

    print("Recurtion:")
    visited = [0] * v
    n = 0
    for i in range(0, v, 1):
        if (visited[i] == 0):
            visited[i] = 1
            DFS_Recurtion(Graph, visited, v, i)
            n = n + 1
    print(n)

MAIN()