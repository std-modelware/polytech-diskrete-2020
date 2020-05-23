import networkx as nx
import matplotlib.pyplot as plt
class Knot:
    def __init__(self, data, indexloc = 0):
        self.data = data
        self.index = indexloc
class GraphMatrix:
    def __init__(self, knots):
        self.matrix = [[0] * len(knots) for _ in range(len(knots))]
        self.knots = knots
        for i in range(len(self.knots)):
            self.knots[i].index = i
    def Connect(self, knot1, knot2, weight = 1):
        self.matrix[knot1.index][knot2.index] = self.matrix[knot2.index][knot1.index] = weight
    def IsConnection(self, knot1, knot2):
        return self.matrix[knot1.index][knot2.index] != 0 or self.matrix[knot2.index][knot1.index] != 0
    def ConnectionFrom(self, knot):
        return [(self.knots[col], self.matrix[knot][col]) for col in range(len(self.matrix[knot])) if self.matrix[knot][col] != 0]
    def DijkstraAlgorithm(self, knot):
        path = [None] * len(self.knots)
        for i in range(len(path)):
            path[i] = [float("inf")]
            path[i].append([self.knots[knot.index]])
        path[knot.index][0] = 0
        queue = [i for i in range(len(self.knots))]
        seen = set()
        while len(queue) > 0:
            min_path = float("inf")
            min_node = None
            for n in queue:
                if path[n][0] < min_path and n not in seen:
                    min_path = path[n][0]
                    min_node = n
            queue.remove(min_node)
            seen.add(min_node)
            connections = self.ConnectionFrom(min_node)
            for (knot, weight) in connections:
                least_path = weight + min_path
                if least_path < path[knot.index][0]:
                    path[knot.index][0] = least_path
                    path[knot.index][1] = list(path[min_node][1])
                    path[knot.index][1].append(knot)
        return path


a = Knot("A")
b = Knot("B")
c = Knot("C")
d = Knot("D")
e = Knot("E")
f = Knot("F")
w_graph = GraphMatrix([a, b, c, d, e, f])
w_graph.Connect(a, b, 7)
w_graph.Connect(a, c, 9)
w_graph.Connect(a, e, 14)
w_graph.Connect(b, c, 10)
w_graph.Connect(b, d, 15)
w_graph.Connect(c, d, 11)
w_graph.Connect(c, f, 2)
w_graph.Connect(d, e, 9)

G = nx.Graph()
e = [('A', 'B', 7),('A', 'C', 9),('A', 'E', 14),('A', 'C', 10),('B', 'D', 15),('C', 'D', 11),('C', 'F', 2),('D', 'E', 9)]
G.add_weighted_edges_from(e)
edge_labels = dict( ((u, v), d["weight"]) for u, v, d in G.edges(data=True) )
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
plt.show()

print('Shortless way from b to...')
for (weight, knot) in w_graph.DijkstraAlgorithm(b):
    print(knot[len(knot) - 1].data, '=')
    print(weight,  [n.data for n in knot])

