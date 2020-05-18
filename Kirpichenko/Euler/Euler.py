import numpy as np
import random
import copy
import matplotlib.pyplot as plot

def fix_graph(graph):
    i = 0
    while i < len(graph):
        if len(graph[i]) == 0:
            graph[i - 1].append(i)
            graph[i].append(i - 1)
            i = -1
        elif len(graph[i]) % 2 != 0:
            fixed = False
            for j in range(i + 1, n):
                if (len(graph[j]) % 2 != 0 or len(graph[j]) == 0) and j not in graph[i]:
                    graph[i].append(j)
                    graph[j].append(i)
                    fixed = True
                    break
            if not fixed:
                if len(graph[i]) != len(graph) - 1:
                    while True:
                        v = random.randint(0, n - 1)
                        if v not in graph[i] and v != i:
                            graph[i].append(v)
                            graph[v].append(i)
                            break
                else:
                    v = random.randint(0, n - 1)
                    while v == i:
                        v = random.randint(0, n - 1)
                    graph[i].remove(v)
                    graph[v].remove(i)
                i = -1
        i += 1


def gener_euler_graph(n):
    graph = []
    for i in range(0, n):
        graph.append([])
    for i in range(0, n - 3):
        links_num = random.randrange(2, n - i, 2)
        for j in range(0, links_num):
            while True:
                v = random.randint(i + 1, n - 1)
                if v not in graph[i] and v != i:
                    graph[i].append(v)
                    graph[v].append(i)
                    break
    fix_graph(graph)
    return graph


def find_euler_cycle(G):
    stack = []
    cycle = []
    graph = copy.deepcopy(G)
    stack.append(graph[0][0])
    while len(stack) != 0:
        v = stack[-1]
        if len(graph[v]) == 0:
            cycle.append(v)
            stack.pop()
        else:
            u = graph[v][0]
            stack.append(u)
            graph[v].remove(u)
            graph[u].remove(v)
    return cycle


def get_poly_points(n, r=1):
    x = []
    y = []
    angle = np.pi - (n-2) * np.pi / n
    for i in range(n):
        x.append(r * np.cos(i * angle))
        y.append(r * np.sin(i * angle))
    return x, y


def draw_graph(graph, cycle):
    x, y = get_poly_points(n)
    plot.figure(figsize=(6, 6))
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            plot.plot([x[i], x[graph[i][j]]], [y[i], y[graph[i][j]]], c='b')
    for i in range(0, len(cycle) - 1):
        plot.plot([x[cycle[i]], x[cycle[i + 1]]], [y[cycle[i]], y[cycle[i + 1]]], c='r',  ls=':', lw=2.5)
    plot.scatter(x, y, c='b', s=100)


n = 10 # number of vertices
euler_graph = gener_euler_graph(n)
print("Graph, represented in adjacency lists:")
print(euler_graph)
cycle = find_euler_cycle(euler_graph)
print("Euler cycle of this graph:")
print(cycle)
draw_graph(euler_graph, cycle)
plot.show()
plot.close()

