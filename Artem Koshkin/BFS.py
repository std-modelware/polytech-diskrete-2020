"""A stroke is a sequential visit (processing) of the graph vertices
 in a certain order. One of the two commonly used methods of traversal
 is a breadth-first search.The essence of BFS is quite simple. The crawl
 begins with visiting a specific vertex (an arbitrary vertex is often
 selected to crawl the entire graph). Then the algorithm visits the neighbors
 of this vertex. Behind them-neighbors of neighbors, and so on."""

""" Here is an adjacency matrix 
    that you can change"""
adj = [[1, 3],  # zero vertex
       [0, 3, 4, 5],  # first vertex
       [4, 5],  # second vertex
       [0, 1, 5],  # third vertex
       [1, 2],  # fourth vertex
       [1, 2, 3]  # fifth vertex
       ]

level = [-1] * len(adj)  # a list of levels of the vertices


def BFS(s):
    global level
    level[s] = 0  # level of the initial vertex
    queue = [s]  # adding the starting vertex to the queue
    while queue:  # while there is something there
        v = queue.pop(0)  # extracting the vertex
        for w in adj[v]:  # starting a crawl from vertex v
            if level[w] == -1:  # check for illumination
                queue.append(w)  # adding a vertex to the queue
                level[w] = level[v] + 1  # count the level of the top


for i in range(len(adj)):  # in case there are multiple connectivity components
    if level[i] == -1:
        BFS(i)

"""To check, output the level of each vertex in the graph"""
print(level[0])
print(level[1])
print(level[2])
print(level[3])
print(level[4])
print(level[5])
