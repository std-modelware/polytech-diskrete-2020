#Во входном файле в первой строчке вводится число узлов в графе, в следующих строках написаны списки смежности (начиная с 1. номера вершин графа), если у этой вершины пустой список смежности, то напишите 0.
#В выходном файле в каждой строке написана компонента связности графа

from itertools import groupby

def check(ms):
    for s in C:
        if s.find(ms) != -1:
            return 0
    return 1

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
                        if check(M[v])==1:
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


Г = {}
f = open('C://txt//5.txt','r')
n = int(f.readline())
for i in range(n):
    Г[i+1] = f.readline()
    Г[i+1] = Г[i+1].rstrip('\n')

C = list()
M = {}
e = {}
for i in range(n):
    M[i + 1] = str(i + 1)
    e[i + 1] = int(0)
V = [i + 1 for i in range(n)]
while (len(V) != 0):
    T = list()
    T.append(V[0])
    e[V[0]] = 1
    KCC()
#print(C)
f1 = open('C://txt//5out.txt', 'w')
for sc in C:
    sc+='\n'
    f1.write(sc)
f.close()
f1.close()
