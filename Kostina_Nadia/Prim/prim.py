import heapq

with open("input.txt", "r") as file:
    n, m, = (int(s) for s in file.readline().strip().split())
    graph = [[] for i in range(n)]
    for line in file:
        u, v, weight = (int(s) for s in line.strip().split())
        graph[u - 1].append((weight, u - 1, v - 1))
        graph[v - 1].append((weight, v - 1, u - 1))

visited = [0 for i in range(n)]
visited[0] = 1

heap = graph[0]
heapq.heapify(heap)

mst = []

res = 0

for i in range(n - 1):
    w_min, u, v = heapq.heappop(heap)
    while visited[v]:
        w_min, u, v = heapq.heappop(heap)
    mst.append((u, v))
    res += w_min
    visited[v] = 1

    for tup in graph[v]:
        heapq.heappush(heap, tup)


# Записывает вес остова и ребра

with open("output.txt", 'w') as file:
    file.write(str(res) + '\n')

    for (u, v) in mst:
        file.write(str(u + 1) + " " + str(v + 1) + '\n')
