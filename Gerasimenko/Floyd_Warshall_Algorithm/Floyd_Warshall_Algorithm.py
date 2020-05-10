import sys

INF = sys.maxsize

def ReadGraph(FileWithGraph):
    Graph = []
    i = -1
    j = -1
    for line in FileWithGraph:
        if(line == "Another graph\n"):
            Graph.append([])
            j = j + 1
            continue
        elif(line != '\n'):
            Graph[j].append([])
            for col in line.split():
                if(col == 'inf'):
                    Graph[j][++i].append(INF)
                else:
                    Graph[j][++i].append(int(col))
    return Graph


def FloydWarshall(FileWithGraph):

    graph = ReadGraph(FileWithGraph)

    for t in range(graph.__len__()):
        for k in range(graph[t].__len__()):
            for i in range(graph[t].__len__()):
                for j in range(graph[t].__len__()):
                        graph[t][i][j] = min(graph[t][i][j], graph[t][i][k] + graph[t][k][j])

    # Проверка на то, имеет ли получившийся список графов с минимальными расстояниями граф с отрицательным циклом
    for t in range(graph.__len__()):
        for i in range(graph[t].__len__()):
            if(graph[t][i][i] < 0):
                graph[t] = "negative cycle"
                break
    return graph


def WriteSolution(graph):
    OutputFile = open("output.txt", "w")
    for t in range(graph.__len__()):
        OutputFile.write("\nAnother graph\n")
        if(graph[t] == "negative cycle"):
            OutputFile.write("\nHave got negative cycle\n")
            continue
        for i in range(len(graph[t])):
            for j in range(len(graph[t][i])):
                if(graph[t][i][j] == INF):
                    OutputFile.write("inf ")
                else:
                    OutputFile.write("{:3d} ".format(graph[t][i][j]))
            OutputFile.write("\n")
    OutputFile.close()



# MAIN
f = open('Graph.txt')
result = FloydWarshall(f)
WriteSolution(result)
f.close()
