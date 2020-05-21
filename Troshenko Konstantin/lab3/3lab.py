from random import randint

def EulerCycle(AdjList):
    S = []
    result = []
    v = randint(0, len(AdjList) - 1)
    S.append(v)
    while len(S) > 0:
        v = S[-1]
        if len(AdjList[v]) == 0:
            v = S.pop(-1)
            result.append(v)
        else:
            u = AdjList[v][0]
            S.append(u)
            AdjList[v].remove(u)
            AdjList[u].remove(v)
    return result

AdjList = []

with open('EulerGraph.txt', 'r') as file:
    for line in file:
        AdjList.append([int(i) for i in line.split()])

print(*EulerCycle(AdjList))
