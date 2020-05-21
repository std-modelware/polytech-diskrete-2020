import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def ReadGraph(fileName):
    file = open(fileName)
    line = file.readline()
    vertNumber = int(line)
    graph = [[] for i in range(vertNumber)]

    for line in file:
        verts = list(map(int, line.split()))

        graph[verts[0]].append(verts[1])
        graph[verts[1]].append(verts[0])
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


vertComp = {}
graph = ReadGraph("Test3.txt")
currComp = 0

for vert in range(len(graph)):
    if vert not in vertComp:
        DFS(vert, graph, vertComp, currComp)
        currComp += 1

nxGraph = CreateNxGraph(graph)
nx.draw(nxGraph, pos = nx.spring_layout(nxGraph), labels = vertComp);
plt.show()
