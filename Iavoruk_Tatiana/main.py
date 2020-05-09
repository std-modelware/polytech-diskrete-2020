
from itertools import groupby

def KCC():
    if (len(T) == 0):
        return
    v = T.pop()
    T.append(v)
    if Г[v] == '0':
        C.append(M[v])
        T.pop()
        V.remove(v)
        #KCC()
        return
    else:
        for u in (Г[v].split()):
            if e[int(u)] == 0:
                T.append(int(u))
                e[int(u)] = 1
            else:
                while True:
                    # print(T)
                    if (len(T)==0):
                        C.append(M[v])#для добавления последнего цикла
                        return
                    w = T.pop()
                    V.remove(w)

                    k = set([el for el, _ in groupby(list(Г[int(u)] + " " + Г[w]))])
                    k.remove(' ')
                    # list(k).sort()

                    Г[int(u)] = ' '.join(k)
                    k = set([el for el, _ in groupby(list(M[int(u)] + " " + M[w]))])
                    k.remove(' ')
                    M[int(u)] = ' '.join(k)

                    if int(u) == w:
                        break

                T.append(w)
                V.append(w)
            KCC()


n = int(input("Количество вершин графа "))
#n = 4
Г = {}
for i in range(n):
   print("список смежности", i + 1, "вершины, если их нет напишите 0. Вершишы пишите через пробел.")
   Г[i + 1] = input()
# check()
# Г[1] = '0'
# Г[2] = '3'
# Г[3] = '2'
# Г[4] = '0'
C = list()
M = {}
e = {}
for i in range(n):
    M[i + 1] = str(i + 1);
    e[i + 1] = int(0);
V = [i + 1 for i in range(n)]
while (len(V) != 0):
    T = list()
    T.append(V[0])
    e[V[0]] = 1
    KCC()
print(C)

