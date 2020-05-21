#Алгоритм находит расстояние от одной вершины графа до другой
#Граф описывается списком смежности
#Пример
#Input:
#5 7 - n и m
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

n, m = list(map(int, input().split()))  # Вводим n(кол-во вершин) и m(кол-во рёбер)
lst = [[] for i in range(n)]  # Создаем список смежности
for i in range(m):
    u, v = list(map(int, input().split()))  #Описываем ребра двумя вершинами(u и v)
    u -= 1
    v -= 1
    lst[u].append(v)
    lst[v].append(u)
dist = [None] * n  # Созадем список расстояний до вершин
s, f = list(map(int, input().split()))  #Вводим начальную(s) и конечную(f) вершину
s -= 1
f -= 1
dist[s] = 0
queue = deque([s])  # Создаём очередь из начальной вершины
while len(queue) > 0: 
    top = queue.popleft()
    if top == f:  # Если мы дошли до конечной вершины(f), выводим расстояние до неё
        print(dist[f])  
        exit(0)
    for i in lst[top]:  # Добавляем соседей данной вершины, которых ещё нет в очереди
        if dist[i] is None:
            queue.append(i)
            dist[i] = dist[top] + 1
