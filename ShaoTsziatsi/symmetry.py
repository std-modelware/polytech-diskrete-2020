import matplotlib.pyplot as plt
import numpy as mp
import copy
f = open('C:/Users/shaoj/PycharmProjects/lab_2/result_lab2.txt', 'w')

#Функция: проверить одну последовательность является ли симетрической.
#Если она не симмерична, то return -1
#Если она симметрична, то return индекса Центра симметрии
#Внимание: Для правильного 8-угольного, построенного последовательностью 11110000,
#          его ось симметрия через ни одной точки не проходит.
#          Т.е. при p == 1, программа выходит информацию -1 именно <не симметричная посл-ть>
#          Тогда в случае size % 2 == 0 && колво единицы % 2 == 0, если при p == 1 выходит информацию <не симметричная посл-ть>
#          Не можем сказать "не симметричая посл-ть", еще понадобится проверить при p == 0.
def check_symmetry (arr: list, p: int, size: int):
    flag: int
    i: int = 0
    j: int
    k: int
    l: int
    for i in range(0, size, 1):
        k = (i + 1) % size
        j = (i - p) % size
        flag = -1
        l = 1
        while(l <= (size - 1) / 2):
            if(arr[k] != arr[j]):
                break
            k = (k + 1) % size
            j = (j - 1) % size
            l = l + 1
        if(l > (size - 1) / 2):
            flag = i
            break
    return flag


#Функция : изобразить график
#строка 59 - 71: изобразить ось симметрии
def Paint(arr: list, size: int):
    i: int
    x: list = [0] * (size + 1)
    y: list = [0] * (size + 1)
    h: float = 2*mp.pi / size
    p: int = 1
    flag: int = check_symmetry(arr,p,size)
    if(size % 2 == 0 and arr.count(1) % 2 == 0 and flag == -1):
        p = 0
        flag = check_symmetry(arr,p,size)

    for i in range (0,size + 1,1):
        x[i] = mp.cos(i * h + mp.pi / 2)
        y[i] = mp.sin(i * h + mp.pi / 2)
    plt.plot(x,y,color = "k",linestyle = "--",linewidth = 0.8)
    for i in range (0,size,1):
        if(arr[i] == 1):
            plt.scatter(x[i],y[i],s = 20,color = 'blue')
        else:
            plt.scatter(x[i],y[i],s = 20,color = 'red')

    if(flag != -1):
        if (p == 1 and size % 2 == 0):
            plt.plot([x[flag], x[(flag + size // 2) % size]], [y[flag], y[(flag + size // 2) % size]], color="y",
                     linewidth=0.5)
        if (p == 1 and size % 2 == 1):
            plt.plot([x[flag], (x[(flag + size // 2) % size] + x[(flag - size // 2) % size]) / 2],
                     [y[flag], (y[(flag + size // 2) % size] + y[(flag - size // 2) % size]) / 2], color="y",
                     linewidth=0.5)
        if (p == 0):
            plt.plot([(x[flag] + x[(flag + 1) % size]) / 2, -(x[flag] + x[(flag + 1) % size]) / 2],
                     [(y[flag] + y[(flag + 1) % size]) / 2, -(y[flag] + y[(flag + 1) % size]) / 2], color="y",
                     linewidth=0.5)
    plt.show()


# total: массив массивов: напр:[[1,1,0,0],[1,0,1,0]], содержащий всевозможные неповторяющие после-ти.
# Если в total нет текущего массива, то выходим flag = 1 (not in)
# Иначе flag = 0 (in)
def check (total: list, arr: list, size: int):
    flag: int = 1
    i: int
    j: int
    temp : list = [0] * size
    for i in range (0,size,1):
        for j in range(0,size,1):
            temp[j] = arr[(i + j) % size]
        if(temp in total):
            flag = 0
            break
    return flag


# Алгоритм с возвратом, по-англ: Depth-first search
# void DFS(Vertex v)
# {
#     visited[v] = True
#     for (каждая соседняя точка w) if(visited[w] == 0) {DFS(W)}
# }
# Перебор всевозможных комбинаций при заданной длине массива и количестве "1"
# Внимание: из-за можно сдвигаться, то мы можем всегда поставить "1" в первом месте массива
def Traverse(total: list, arr: list, visited: list, quantity1: int, m: int, size: int):
    i: int
    for i in range(1,size,1):
        if(visited[i] == 0):
            visited[i] = 1
            arr[i] = 1
            if(m == quantity1):
                if(check(total,arr,size) == 1):
                    total.append(copy.deepcopy(arr))
                visited[i] = 0
                arr[i] = 0
                continue
            Traverse(total,arr,visited,quantity1,m + 1,size)
            arr[i] = 0
            visited[i] = 0

def mmaaiinn():
    n: int
    j: int
    k: int
    i: int
    total: list
    arr: list
    visited: list
    for n in range(6,16,1):
        for k in range(3,n // 2 + 1,1):
            if(n == 15 and k > 6): continue
            total = []
            arr = [0] * n
            arr[0] = 1
            visited = [0] * n
            visited[0] = 1
            i = 0
            Traverse(total,arr,visited,k,2,n)
            for j in range(0,len(total),1):
                if(check_symmetry(total[j],1,n) != -1): i = i + 1
                elif (n % 2 == 0 and k % 2 == 0 and check_symmetry(total[j],0,n) != -1): i = i + 1
            f.write("n == %d  k == %d  N == %d  M == %d\n" %(n,k,len(total),i))



mmaaiinn()
f.close()