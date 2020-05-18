# РЕАЛИЗАЦИЯ АЛГОРИТМА ПОИСКА НАИБОЛЬШЕГО ПАРОСОЧЕТАНИЯ В ДВУДОЛЬНОМ ГРАФЕ

# список пройденных и непройденных вершин
x = list()
# список смежности
g = list()
# список ребер, образующих максимальное паросочетание
M = list()

# поиск в глубину
def Aug(v: int):
    if x[v] == True:
        return False
    x[v] = True
    for i in range(len(g[v])):
        u = g[v][i]
        if M[u] == -1 or Aug(M[u]):
            M[u] = v
            return True
        i = 0
    return False


# поиск наибольшего паросочетания
def MaxMatch(n1: int):
    for i in range(1, n1 + 1):
        for j in range(n1 + 1):
            x.insert(j, False)
        Aug(i)

# вывод наибольшего паросочетания
def Print(n2: int):
    print('Наибольшее паросочетание:')
    for i in range(1, n2 + 1):
        if M[i] != -1:
            print(M[i], i)

def Search(G: list, g: list, n1: int, n2: int):
    print('Граф:')
    print('Количество вершин в первой доле - ', n1, ',', 'количество вершин во второй доле - ', n2)
    print('Ребра графа:')
    print(G)
    for i in range(n2 + 1):
        M.insert(i, -1)
    MaxMatch(n1)
    Print(n2)
    x.clear()
    M.clear()
    g.clear()

# пример 1
print('Пример 1')
n1 = 3  # количество вершин первой доли
n2 = 3  # количество вершин второй доли
m = 6  # количество ребер
G = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]   # список ребер
g = [[] for i in range(n1 + 1)]
for i in range(m):
    v = G[i][0]
    w = G[i][1]
    g[v].append(w)
Search(G, g, n1, n2)

# пример 2
print('Пример 2')
n1 = 5
n2 = 4
m = 8
G = [[1, 1], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4]]
g = [[] for i in range(n1 + 1)]
for i in range(m):
    v = G[i][0]
    w = G[i][1]
    g[v].append(w)
Search(G, g, n1, n2)
