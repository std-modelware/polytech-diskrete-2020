# Задача с сайта LeetCode Course Schedule(ссылка - https://leetcode.com/problems/course-schedule-ii/)
# На вход дается число курсов  и упорядоченные пары вершин в виде ['курс который можно пройти после курса справа','курс который унжно пройти перед курсом слева']
# Формат ввода: 4, [[1,0],[2,0],[3,1],[3,2]]
# Формат вывода: [0,1,2,3] или [] (в случае если пройти курсы не представляется возможным
# Обход осуществляется через алгоритм depth-first search, или обходом в глубину
# Искомый путь записывается в глобальную переменную, чтобы не таскать ее с собой в каждой функции
path = []

def CheckCourse(course, graph, visited):
    if (visited[course] == 2): # вершина окрашена в черный цвет
        return 1
    if (visited[course] == 1): # вершина окрашена в серый цвет
        return 0
    visited[course] = 1 # не заходили в вершину до этого, меняем ее цвет с белого на черный
    for prevCourse in graph[course]:
        flag = CheckCourse(prevCourse, graph, visited)
        if (flag == False):
            return False
    visited[course] = 2
    path.append(course)
    return True

def Graph(n, array):
    i = 0
    graph = [0] * n
    for i in range(n):
        graph[i] = []
    i = 0
    while (i < len(array)):
        graph[array[i][0]].append(array[i][1])
        i += 1
    #print(graph) # отладочный вывод
    return graph


def PathFinder(n, array):
    i = 0
    visited = [0 for i in range(n)]
    graph = Graph(n, array)
    while (i < n):
        flag = CheckCourse(i, graph, visited)
        if (flag == False):
            return False
        i += 1
    return True

def FindOrder(n, courseCouples):
    solved = PathFinder(n, courseCouples)
    if (solved == False):
        return []
    else:
        return path

def BuildCouples(num, strCouples):
    k = 0
    couples = []
    i = 0
    while (i < len(strCouples) - 5):
        couples.append([0] * 2)
        couples[k][0] = int(strCouples[i+3])
        couples[k][1] = int(strCouples[i+5])
        i += 6
        k += 1
    return couples

#str = input() #отладочный вывод
#data = str.split(',', 1) #отладочный вывод
#print(data) #отладочный вывод
#n = int(data[0]) # вырезали число курсов
#print(n) # отладочный вывод

#out = BuildCouples(n, data[1])
#print(out) # отладочный вывод

#res = FindOrder(n, out)
#print(res)

#тест 1
test = "4, [[1,0],[2,0],[3,1],[3,2]]"
data = test.split(',', 1)
print("Тестовые данные теста 1: " + "4, [[1,0],[2,0],[3,1],[3,2]]")
n = int(data[0])
couples = BuildCouples(n, data[1])
res = FindOrder(n, couples)
print(res)

path = [] #очистка результатов предыдущего теста

#тест2
test = "2, [[1,0]]"
data = test.split(',', 1)
print("Тестовые данные теста 2: " + "2, [[1,0]]")
n = int(data[0])
couples = BuildCouples(n, data[1])
res = FindOrder(n, couples)
print(res)

path = [] #очистка результатов предыдущего теста

#тест3
test = "2, [[1,0],[0,1]]"
print("Тестовые данные теста 3: " + "2, [[1,0],[0,1]]")
data = test.split(',', 1)
n = int(data[0])
couples = BuildCouples(n, data[1])
res = FindOrder(n, couples)
print(res)

path = [] #очистка результатов предыдущего теста

#тест4
test = "3, [[1,0],[2,1]]"
print("Тестовые данные теста 4: " + "3, [[1,0],[2,1]]")
data = test.split(',', 1)
n = int(data[0])
couples = BuildCouples(n, data[1])
res = FindOrder(n, couples)
print(res)

path = [] #очистка результатов предыдущего теста







