import matplotlib.pyplot as plt
import numpy as mp
import copy
f = open('C:/Users/shaoj/PycharmProjects/lab_2/result_lab2.txt', 'w')

#Функция: проверить одну последовательность является ли симетрической.
#Если она не симмерична, то return [] пустой лист
#Если она симметрична, то return лист построенный всевозможными индексами Центра симметрии
#Внимание: Для правильного 8-угольного, построенного последовательностью 11110000,
#          его ось симметрия через ни одной точки не проходит.
#          Т.е. при p == 1, программа выходит информацию -1 именно <не симметричная посл-ть>
#          Тогда в случае size % 2 == 0 && колво единицы % 2 == 0, если при p == 1 выходит информацию <не симметричная посл-ть>
#          Не можем сказать "не симметричая посл-ть", еще понадобится проверить при p == 0.
def check_symmetry (arr: list, p: int, size: int):
    flag: list = []
    i: int = 0
    j: int
    k: int
    l: int
    for i in range(0, size, 1):
        k = (i + 1) % size
        j = (i - p) % size
        l = 1
        while(l <= (size - 1) / 2):
            if(arr[k] != arr[j]):
                break
            k = (k + 1) % size
            j = (j - 1) % size
            l = l + 1
        if(l > (size - 1) / 2):
            flag = flag + [i]
    return flag

#Функция : изобразить график
#строка 55 - 80: изобразить ось симметрии
def Paint(arr: list, size: int):
    i: int
    x: list = [0] * (size + 1)
    y: list = [0] * (size + 1)
    h: float = 2*mp.pi / size
    flag: list = check_symmetry(arr,1,size)

    for i in range (0,size + 1,1):
        x[i] = mp.cos(i * h + mp.pi / 2)
        y[i] = mp.sin(i * h + mp.pi / 2)
    plt.plot(x,y,color = "k",linestyle = "--",linewidth = 0.8)
    for i in range (0,size,1):
        if(arr[i] == 1):
            plt.scatter(x[i],y[i],s = 20,color = 'blue')
        else:
            plt.scatter(x[i],y[i],s = 20,color = 'red')
    x.pop()
    y.pop()

    if(flag != []):
        if(size % 2 == 1):
            for i in range (0,len(flag),1):
                plt.plot([x[flag[i]], (x[(flag[i] + size // 2) % size] + x[(flag[i] - size // 2) % size]) / 2],
                         [y[flag[i]], (y[(flag[i] + size // 2) % size] + y[(flag[i] - size // 2) % size]) / 2], color="y",
                         linewidth=0.5)
        else:
            for i in range(0, len(flag), 1):
                plt.plot([x[flag[i]], x[(flag[i] + size // 2) % size]], [y[flag[i]], y[(flag[i] + size // 2) % size]],
                         color="y",linewidth=0.5)
            if(arr.count(1) % 2 == 0):
                flag = check_symmetry(arr, 0, size)
                if (flag != []):
                    for i in range(0, len(flag), 1):
                        plt.plot(
                            [(x[flag[i]] + x[(flag[i] + 1) % size]) / 2, -(x[flag[i]] + x[(flag[i] + 1) % size]) / 2],
                            [(y[flag[i]] + y[(flag[i] + 1) % size]) / 2, -(y[flag[i]] + y[(flag[i] + 1) % size]) / 2],
                            color="y", linewidth=0.5)
    else:
        if(size % 2 == 0 and arr.count(1) % 2 == 0):
            flag = check_symmetry(arr, 0, size)
            if (flag != []):
                for i in range(0, len(flag), 1):
                    plt.plot([(x[flag[i]] + x[(flag[i] + 1) % size]) / 2, -(x[flag[i]] + x[(flag[i] + 1) % size]) / 2],
                             [(y[flag[i]] + y[(flag[i] + 1) % size]) / 2, -(y[flag[i]] + y[(flag[i] + 1) % size]) / 2],
                             color="y",linewidth=0.5)
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
def Traverse(total: list, arr: list, visited: list, quantity1: int, m: int, size: int):
    i: int
    for i in range(0,size,1):
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
    n: int = int(input())
    k: int = int(input())
    if(n <= 2 or 2*k > n or n >= 16):
        f.write("ERROR: incorrect parameter")
        f.close()
        return

    i: int
    j: int
    l: int
    total: list = []
    arr: list = [0]*n
    visited: list = [0]*n
    temp: list
    Traverse(total,arr,visited,k,1,n)
    for i in range(0, len(total), 1):
        temp = check_symmetry(total[i],1,n)
        if(temp != []):
            if (n % 2 == 1):
                f.write("%s     %d\n" % (total[i], len(temp)))
                for j in range(0, len(temp), 1):
                    f.write("%d|" % total[i][(temp[j]) % n])
                    for l in range(0, (len(total[i]) - 1) // 2, 1):
                        f.write("%d" % total[i][(temp[j] + l + 1) % n])
                    f.write("|")
                    for l in range((len(total[i]) - 1) // 2, len(total[i]) - 1, 1):
                        f.write("%d" % total[i][(temp[j] + l + 1) % n])
                    f.write("\n")
            else:
                if(total[i].count(1) % 2 == 0):
                    f.write("%s     %d\n" % (total[i], len(temp + check_symmetry(total[i], 0, n))))
                else:
                    f.write("%s     %d\n" % (total[i], len(temp)))

                for j in range(0, len(temp), 1):
                    f.write("%d|" % total[i][(temp[j]) % n])
                    for l in range(0, len(total[i]) // 2 - 1, 1):
                        f.write("%d" % total[i][(temp[j] + l + 1) % n])
                    f.write("|")
                    f.write("%d|" % total[i][(temp[j]) % n])
                    for l in range(len(total[i]) // 2 + 1, len(total[i]), 1):
                        f.write("%d" % total[i][(temp[j] + l) % n])
                    f.write("\n")

                if(total[i].count(1) % 2 == 0):
                    temp = check_symmetry(total[i], 0, n)
                    if (temp != []):
                        for j in range(0, len(temp), 1):
                            for l in range(0, len(total[i]) // 2, 1):
                                f.write("%d" % total[i][(temp[j] + l + 1) % n])
                            f.write("    |    ")
                            for l in range(len(total[i]) // 2, len(total[i]), 1):
                                f.write("%d" % total[i][(temp[j] + l + 1) % n])
                            f.write("\n")
        else:
            if((n % 2 == 0 and total[i].count(1) % 2 == 0) == False):
                f.write("%s     %d\n" % (total[i], len(temp)))
            else:
                temp = check_symmetry(total[i], 0, n)
                f.write("%s     %d\n" % (total[i], len(temp)))
                if(temp != []):
                    for j in range(0, len(temp), 1):
                        for l in range(0, len(total[i]) // 2, 1):
                            f.write("%d" % total[i][(temp[j] + l + 1) % n])
                        f.write("    |    ")
                        for l in range(len(total[i]) // 2, len(total[i]), 1):
                            f.write("%d" % total[i][(temp[j] + l + 1) % n])
                        f.write("\n")

mmaaiinn()