import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain
from collections import deque
from copy import copy, deepcopy


class Graph:

    def __init__(self, adj_matrix):
        row, col = adj_matrix.shape
        self.adj_list = None

        # check matrix symmetry
        if not (adj_matrix == adj_matrix.T).all():
            return

        # graph stored as an adjacency list
        self.adj_list = [[] for _ in range(row)]
        for index, elem in np.ndenumerate(adj_matrix):
            if elem:
                self.adj_list[index[0]].append(index[1])

    # dfs traverse, returns:
    # is_tree if graph is a tree
    # node with max way from start
    def dfs(self, node_start):
        if self.adj_list is None:
            return None, None
        is_loops = 0
        visited_nodes = len(self.adj_list) * [0]

        stack_to_visit = deque()
        stack_to_visit.append((node_start, -1, 0))

        node_max_way, max_way = (node_start, 0)

        while stack_to_visit:
            cur_node, prev_node, way_len = stack_to_visit.pop()

            # check if node was visited before
            if visited_nodes[cur_node]:
                is_loops = 1
            else:
                visited_nodes[cur_node] = 1

                if max_way < way_len:
                    node_max_way = cur_node
                    max_way = way_len

                for adj_node in self.adj_list[cur_node]:
                    if adj_node != prev_node:
                        stack_to_visit.append((adj_node, cur_node, way_len + 1))

        is_linked = all(visited_nodes)
        is_tree = is_linked and not is_loops
        return is_tree, node_max_way

    # find a path between vertexes 'node_start' and 'node_end'
    def find_path(self, node_start, node_end):
        if self.adj_list is None:
            return None
        visited_nodes = len(self.adj_list)*[0]
        current_path = []
        self.__recursive_path_search_dfs(node_start, node_end, visited_nodes, current_path)
        return current_path

    # recursive function of finding the path between vertexes by DFS alg
    def __recursive_path_search_dfs(self, node_cur, node_end, visited_nodes, current_path):
        # if already visited, return
        if visited_nodes[node_cur]:
            return 0
        # else mark node as visited
        else:
            visited_nodes[node_cur] = 1

        if node_cur == node_end:
            current_path.append(node_cur)
            return 1

        for adj_node in self.adj_list[node_cur]:
            # if the path was found, append to path list and return
            if self.__recursive_path_search_dfs(adj_node, node_end, visited_nodes, current_path):
                current_path.append(node_cur)
                return 1
        return 0


class Tree:

    def __init__(self, graph):
        is_tree, max_node1 = graph.dfs(0)

        if not is_tree:
            self.root = None
            return
        _, max_node2 = graph.dfs(max_node1)
        # longest path in tree
        diameter_path = graph.find_path(max_node1, max_node2)

        # tree stored as an adjacency list
        self.adj_list = deepcopy(graph.adj_list)

        # if tree's diameter is odd, then
        # root of the tree is mid element of this path
        if len(diameter_path) % 2:
            self.root = diameter_path[int(len(diameter_path) / 2)]

        # if diameter is even, then create new vertex -1
        # as a root between two middle elements of diameter path
        else:
            self.root = -1
            # vertices adjacent to root: mid elements of diameter path
            adj_root = [diameter_path[int(len(diameter_path) / 2 - 1)], diameter_path[int(len(diameter_path) / 2)]]
            self.adj_list.append(adj_root)
            # add edges with root '-1' and remove edge between mid elements
            self.adj_list[adj_root[0]].remove(adj_root[1])
            self.adj_list[adj_root[0]].append(-1)
            self.adj_list[adj_root[1]].remove(adj_root[0])
            self.adj_list[adj_root[1]].append(-1)

    # return -1 if some graph is not a tree
    # 0 if trees are not isomorphic
    # 1 if trees are isomorphic
    def isomorphic(self, tree):
        # check if it is valid trees
        if self.root is None or tree.root is None:
            return -1
        #
        if self.root * tree.root < 0:
            return 0

        return self.__encode() == tree.__encode()

    # return complete invariant of a tree
    # (list of digits)
    # realization based on paper:
    # https://logic.pdmi.ras.ru/~smal/files/smal_jass08.pdf
    def __encode(self):
        return self.__recursive_encode(self.root, -5112)

    def __recursive_encode(self, node, parent_node):
        children = list(self.adj_list[node])
        if parent_node in self.adj_list[node]:
            children.remove(parent_node)

        if children:
            children_codes = []
            for node_child in children:
                children_codes.append(self.__recursive_encode(node_child, node))
            children_codes.sort(key=len)
            return [1] + list(chain.from_iterable(children_codes)) + [0]
        else:
            return [1, 0]


# function for checking if two trees are isomorphic
# return -1 if some graph is not tree
# 0 if trees are not isomorphic
# 1 if trees are isomorphic
def check_isomorphism(matrix1, matrix2):
    graph1 = Graph(matrix1)
    tree1 = Tree(graph1)

    graph2 = Graph(matrix2)
    tree2 = Tree(graph2)

    return tree1.isomorphic(tree2)


# draw adjacency matrix
def draw_matrix(matrix):
    plt.imshow(matrix,
               cmap='Greys', interpolation='none', aspect='equal')
    row, col = matrix.shape
    ax = plt.gca()
    ax.set_xticks(np.arange(0, col, 1))
    ax.set_yticks(np.arange(0, row, 1))

    ax.set_xticks(np.arange(-.5, col, 1), minor=True)
    ax.set_yticks(np.arange(-.5, row, 1), minor=True)

    ax.xaxis.tick_top()

    ax.grid(which='minor', color='grey', linestyle='-', linewidth=2)


# take the input from directory 'file_path'
# return the answer as .png image stored in this directory
def compare_graphs(file_path):
    matrix1 = np.loadtxt(file_path+'graph_1.txt')
    matrix2 = np.loadtxt(file_path+'graph_2.txt')

    G1 = nx.from_numpy_array(matrix1)
    G2 = nx.from_numpy_array(matrix2)

    fig = plt.figure()
    plt.subplot(221)
    plt.title('Graph N1')
    draw_matrix(matrix1)
    plt.subplot(222)
    plt.title('Graph N2')
    draw_matrix(matrix2)
    plt.subplot(223)
    nx.draw_kamada_kawai(G1, with_labels=True)
    plt.subplot(224)
    nx.draw_kamada_kawai(G2, with_labels=True)

    answer = ''
    res = check_isomorphism(matrix1, matrix2)
    if res < 0:
        answer = 'Some graph is not a tree'
    if res == 0:
        answer = 'Trees are not isomorphic'
    if res > 0:
        answer = 'Trees are isomorphic'
    plt.gcf().suptitle(answer, fontsize=10, y=0.05)
    plt.show()

    fig.savefig(file_path+'answer.png')


def main():
    compare_graphs('.\\Tests\\isomorphic_1\\')
    compare_graphs('.\\Tests\\isomorphic_2\\')
    compare_graphs('.\\Tests\\isomorphic_3\\')

    compare_graphs('.\\Tests\\not_isomorphic_1\\')
    compare_graphs('.\\Tests\\not_isomorphic_2\\')
    compare_graphs('.\\Tests\\not_isomorphic_3\\')

    compare_graphs('.\\Tests\\not_trees_1\\')
    compare_graphs('.\\Tests\\not_trees_2\\')
    compare_graphs('.\\Tests\\not_trees_3\\')


main()
