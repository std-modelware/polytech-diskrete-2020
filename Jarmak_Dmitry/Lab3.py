import sys
# Лабораторная работа № 3. Изначальный граф задается списком смежности.
# Первый параметр отвечает за количество вершин, далее по строкам записаны его ориентированные связи


class Stack:    # Собственный класс для стека
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def top(self):
        return self.arr[len(self.arr) - 1]

    def is_empty(self):
        return self.arr == []


def last(C: list, item):   # Проверка на последний компонент связанности
    for pos in C:
        if item == pos:
            return False
    return True


def union(one, two):  # Вспомогательная функция объединения множеств
    k = len(one)
    d = len(two)
    res = set()

    if one == two:
        return one

    for i in two:
        one.append(i)
    for i in one:
        res.add(i)

    string = []
    s_out = []
    check = []

    for i in one:
        string.append(i)
        if string[0] in res and string[0] in check:
            string.clear()
        else:
            s_out.append(string[0])
            check.append(string[0])
            string.clear()

    return s_out


def SCC(G: dict, M: dict, T: Stack, C: list, V: list, e: list):
    if T.is_empty():   # Негде выделять
        return
    v = T.top()        # Верхний узел на стеке
    if G[v][0] == '0':
        C.append(M[v])   # это КСС, удалить узел, снять узел v со стека
        V.remove(v)
        T.pop()
        return      # Возврат из тупика
    else:
        for u in G[v]:
            if e[int(u)] == 0:
                T.push(int(u))   # положить узел u в стек и отметить
                e[int(u)] = 1
            else:
                while True:
                    if T.is_empty():   # Нужно отдельно проверить случай, когда стэк пуст
                        if last(C, M[v]):
                            C.append(M[v])
                        return

                    w = T.pop()
                    V.remove(w)
                    G[int(u)] = union(G[int(u)], G[w])
                    M[int(u)] = union(M[int(u)], M[w])

                    if int(u) == w:
                        break

                T.push(w)  # Возвращаем узел, с которого начали
                V.append(w)
            SCC(G, M, T, C, V, e)  # Поиск в глубину


def find_scc(G: dict, size: int):
    C = list()
    M = {}
    app = []
    e = [0] * (size + 1)    # Необходимо, чтобы помечать уже посещенные вершины

    for i in range(size):
        app.append(str(i + 1))
        M.update({i + 1: app.copy()})   # M[v] список узлов, входящих в ту же КСС, что и v
        app.clear()

    V = [i + 1 for i in range(size)]
    while len(V) != 0:
        T = Stack()    # взять v , положить в стек
        T.push(V[0])
        e[V[0]] = 1
        SCC(G, M, T, C, V, e)    # отметить e и вызвать процедуру КСС

    return C


def main():
    G = {}
    size = 0

    try:
        file = open('graph7.txt', 'r')
        size = int(file.readline())

        for i in range(size):
            G[i + 1] = file.readline().split()

        file.close()
    except IOError:
        print("Could not open file!")

    print(G)
    # Функция нахождения компонент сильной связанности в орграфе, описана в пособии Новикова Ф. А. на стр. 1221-1222
    if size != 0:
        C = find_scc(G, size)
        print(C)

        try:
            file = open('graph_out.txt', 'w')
            for pos in C:
                file.write("G -> (%s) " % pos)
            file.close()
        except IOError:
            print("Could not open file!")


if __name__ == "__main__":
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main()
