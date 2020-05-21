#Считает степень вершины
def Deg(Vertex, Ribs):
    deg = 0
    for Rib in Ribs:
        if Rib[0] == Vertex or Rib[1] == Vertex:
            deg += 1
    return deg

#На ходит ребра смежный с Rib в списке ребер Ribs
def FindAdjacentRibs(Rib, Ribs):
    AdjacentRibs = []
    for Rib_i in Ribs:
        # Если рассматривать ребра как множества из двух вешин,
        # то они будуд смежными т. и т. т. когда их объединение равно 3
        if len(set(Rib).union(set(Rib_i))) == 3:
            AdjacentRibs.append(Rib_i)
    return AdjacentRibs

def CheckCycleExistence(VertexNumber, Ribs):
    # Проверка четноси кратностей всех ребер
    OddVertex  = True
    for Vertex in range(VertexNumber):
        if Deg(Vertex, Ribs) % 2 != 0:
            OddVertex = False

    CounеСonnected = True
    # Если граф пустой он не является эйлеровым
    if not Ribs:
        return False
    CloneRibs = Ribs[:]
    RibsToCheck = [CloneRibs[0]]

    # Этот цикл проверяет связность графа
    # Если доставать из RibsToCheck и класть в него смежные с только что иъзятым
    # ребра которые ещё остались в CloneRibs,
    # в случае связного графа, первым опустеет список CloneRibs
    # в случае несвязного, RibsToCheck
    while True:
        if not CloneRibs:
            CounеСonnected = True
            break
        if not RibsToCheck:
            CounеСonnected = False
            break
        CurrentRib = RibsToCheck.pop(0)
        CloneRibs.remove(CurrentRib)
        RibsToCheck.extend(FindAdjacentRibs(CurrentRib, CloneRibs))

    return OddVertex and CounеСonnected

def FindEulerianCycle(Vertexes, Ribs):
    if not CheckCycleExistence(len(Vertexes), Ribs):
        return []
    EulerianCycle = []
    CloneRibs = Ribs[:]
    VertexToCheck = [Vertexes[0]]
    while VertexToCheck:
        CurrentVertex = VertexToCheck[0]
        AdjacentVertex = False
        for Vertex in Vertexes:
            if ([Vertex, CurrentVertex] in CloneRibs) or ([CurrentVertex, Vertex] in CloneRibs):
                VertexToCheck.insert(0, Vertex)
                if [Vertex, CurrentVertex] in CloneRibs:
                    CloneRibs.remove([Vertex, CurrentVertex])
                else:
                    CloneRibs.remove([CurrentVertex, Vertex])
                AdjacentVertex = True
                break
        if not AdjacentVertex:
            VertexToCheck.remove(CurrentVertex)
            EulerianCycle.insert(0, CurrentVertex)
    return EulerianCycle


VertexNumber, RibNumber = map(int, input().split())

Ribs = []
for _ in range(RibNumber):
    u1, u2 = map(int, input().split())
    Ribs.append([u1, u2])


EulerianCycle = FindEulerianCycle(list(range(1, VertexNumber + 1)), Ribs)
if not EulerianCycle:
    print("В графе нет Эйлерова цикла")
else:
    for Vertex in EulerianCycle:
        print(Vertex, end=" ")
