class Edge:
    point1 = str()
    point2 = str()
    len = int()

    def __init__(self, p1:str, p2:str, len:float):
        self.point1 = p1
        self.point2 = p2
        self.len = len

    def __lt__(self, other):
        return float(self.len) < float(other.len)

    def __le__(self, other):
        return float(self.len) <= float(other.len)

    def __eq__(self, other):
        return float(self.len) == float(other.len)

    def __gt__(self, other):
        return float(self.len) > float(other.len)

    def __ge__(self, other):
        return float(self.len) >= float(other.len)

    def __repr__(self):
        return "Edge({},{},{})".format(self.point1, self.point2, self.len)

class Tree:
    edges = list()
    vertices = set()

    def __init__(self):
        self.edges = list()
        self.vertices = set()

    def addEdge(self, edge:Edge):
        self.vertices.add(edge.point1)
        self.vertices.add(edge.point2)
        self.edges.append(edge)

    def merge(self, tree):
        self.vertices = self.vertices.union(tree.vertices)
        self.edges += tree.edges

    def isIn(self, vertex:str):
        if (vertex in self.vertices):
            return True
        return False
    def __repr__(self):
        return self.edges.__repr__()

def Crascal(input: list):
    Trees = list()
    input.sort()
    # for all edges
    for edge in input:
        # posiibilities
        # 1) New tree based on this edge
        # 2) Add to existing edge
        # 3) merge trees with edge
        # 4) skip because it leads to cycle
        # check trees
        needNewTree = True
        tree1 = -1
        tree2 = -1
        for indexTree in range(len(Trees)):
            tree = Trees[indexTree]
            numOfPoints = 0

            if tree.isIn(edge.point1):
                numOfPoints += 1
                needNewTree = False
            if tree.isIn(edge.point2):
                numOfPoints += 1
                needNewTree = False

            if (numOfPoints == 2): # possibility 4)
                break
            if (numOfPoints == 1): # possibility 2) or 3)
                if tree1 != -1:
                    tree2 = indexTree
                    break
                else:
                    tree1 = indexTree
        if needNewTree:  #possibility 1)
            Trees.append(Tree())
            Trees[len(Trees) - 1].addEdge(edge)
        if tree1 != -1 and tree2 == -1:  #possibility 2)
            Trees[tree1].addEdge(edge)
        if tree1 != -1 and tree2 != -1: #possibility 3)
            Trees[tree1].addEdge(edge)
            Trees[tree1].merge(Trees[tree2])
            Trees.pop(tree2)
    return Trees[0]


if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.split()
            input.append(Edge(line[0], line[1], line[2]))
    print(Crascal(input))
