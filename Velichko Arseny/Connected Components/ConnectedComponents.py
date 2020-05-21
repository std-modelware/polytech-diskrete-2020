import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def CreateGraph(vertNumber, edgeNumber):
    graph = [[] for i in range(vertNumber)]

    for i in range(edgeNumber):
        firstVert = np.random.randint(0, vertNumber)
        secondVert = np.random.randint(0, vertNumber)

        graph[firstVert].append(secondVert)
        graph[secondVert].append(firstVert)
    return graph

def DFS(vert, graph, vertComp, currComp):
    vertComp[vert] = currComp

    for neighbour in graph[vert]:
        if neighbour not in vertComp:
            DFS(neighbour, graph, vertComp, currComp)

def CreateNxGraph(graph):
    nxGraph = nx.Graph();

    for i in range(len(graph)):
        nxGraph.add_node(i)
        for j in graph[i]:
            nxGraph.add_edge(i, j);
    return nxGraph

print("Input vertex number:")
vertNumber = int(input())
print("Input edges number:")
edgeNumber = int(input())

vertComp = {}
graph = CreateGraph(vertNumber, edgeNumber)
currComp = 0

for vert in range(vertNumber):
    if vert not in vertComp:
        DFS(vert, graph, vertComp, currComp)
        currComp += 1

nxGraph = CreateNxGraph(graph)
nx.draw(nxGraph, pos = nx.spring_layout(nxGraph), labels = vertComp);
plt.show()
