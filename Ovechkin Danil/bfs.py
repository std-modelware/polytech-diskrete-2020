#Алгоритм находит минимальное расстояние от одной вершины графа до другой c помощью поиска в ширину
#Граф описывается списком смежности
#Пример
#Input:
#5 7 - n и m(кол-во врешин и кол-во ребер)
#1 2
#1 3
#1 4
#2 5
#2 4
#3 4
#5 4
#1 5 - start и finish
#Output:
#2
from collections import deque
fp = open("input.txt", "r")

def Read2Number(fp):
    n = fp.read(1)
    while (n == "\n" or n == " "):
        n = fp.read(1)
    n = int(n)

    m = fp.read(1)
    while (m == "\n" or m == " "):
        m = fp.read(1)
    m = int(m)
    return n,m;
def ReadList(fp):
    n, m = Read2Number(fp)
    lst = [[] for i in range(n)]  # Создаем список смежности
    for i in range(m):
        u, v = Read2Number(fp)  # Описываем ребра двумя вершинами(u и v)
        u -= 1
        v -= 1
        lst[u].append(v)
        lst[v].append(u)
    dist = [None] * n  # Созадем список расстояний до вершин
    s, f = Read2Number(fp)  # Вводим начальную(s) и конечную(f) вершину
    s -= 1
    f -= 1
    dist[s] = 0
    return dist, lst, s,f

def BFS(fp):
    dist, lst, s, f = ReadList(fp)
    queue = deque([s])  # Создаём очередь из начальной вершины
    while len(queue) > 0:
        top = queue.popleft()
        if top == f:  # Если мы дошли до конечной вершины(f), выводим расстояние до неё
            return dist[f]
        for i in lst[top]:  # Добавляем соседей данной вершины, которых ещё нет в очереди
            if dist[i] is None:
                queue.append(i)
                dist[i] = dist[top] + 1


print(BFS(fp))
