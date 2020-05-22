# Список смежности, которым задается граф
# Результат - список вершин обхода
matrix = {0: [1, 2, 3], 1: [0, 2, 4],
          2: [0, 1], 3: [0], 4: [1]}

# Поиск в ширину осуществляется на структуре данных очередь
Queue = []


def push(val):
    Queue.append(val)


def pop():
    return Queue.pop(0)


def top():
    return Queue[0]


def size():
    return len(Queue)


def isempty():
    return len(Queue) == 0


def clear():
    Queue[:] = []


temp = []
# Вершины обхода
visited = []

# vertex - вершина, с которой начинается обход - задается пользователем
def BFS(matrix, vertex):
    for i in range(len(matrix)):
        temp.append(0)
    push(vertex)
    # Пока очередь непустая, выполняем обход
    while Queue:
        vertex = top()
        pop()
        # Если вершина просмотрена, то идем дальше
        # иначе просматриваем данную вершину
        if temp[vertex] != 0:
            continue
        visited.append(vertex)
        # Вершина просмотрена - отмечаем единицей
        temp[vertex] = 1
        # Смотрим соседей вершин
        for neighbour in matrix[vertex]:
            # Добавляем в очередь
            push(neighbour)
    return visited

print(BFS(matrix, 4))


# Поиск в глубину осуществляем на структуре данных стек

Stack = []


def push(val):
    Stack.append(val)


def pop():
    return Stack.pop()


def top():
    return Stack[-1]


def size():
    return len(Stack)


def isempty():
    return len(Stack) == 0


def clear():
    Stack[:] = []


# Вершины обхода
visited = []


def DFS(matrix, vertex):
    visited.append(vertex)
    push(vertex)
    # Пока стек непустой, выполняем обход
    while Stack:
        vertex = top()
        # Если данную вершину еще не обошли, то добавляем ее в посещенные и отмечаем единицей
        if vertex not in visited:
            visited.append(vertex)
        visit = 1
        for neighbour in matrix[vertex]:
            # Если мы не встретили ни одной соседней вершины, которая еще не посещена, то значит,
            # Что обход по этой вершине завершен
            # Вытаскиваем ее из стека, иначе обходим дальше
            if neighbour not in visited:
                push(neighbour)
                visit = 0
                break
        if visit == 1:
            pop()
    return visited


print(DFS(matrix, 2))

