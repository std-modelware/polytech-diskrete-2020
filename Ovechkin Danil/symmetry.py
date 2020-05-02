import itertools
#Проверка оси симметрии в многоугольнике
def check_sym(num: list, n: int, cut: str):
    if len(cut) == 0:
        i = n // 2
        j = n // 2 - 1
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    elif len(cut) == 1:
        if num[0] != cut[0]:
            return False
        i = (n - 1) // 2 + 1
        j = i - 1
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    else:
        if num[0] != cut[0] or num[n // 2] != cut[1]:
            return False
        i = n // 2 + 1
        j = i - 2
        while i < n:
            if num[i] != num[j]:
                return False
            i += 1
            j -= 1
    return True

def draw(figures: list):
    for i in figures:
        if len(i[1]) == 0:
            i[0].insert(len(i[0]) // 2, '|')
        else:
            i[0].insert(1, ')')
            i[0].insert(0, '(')
            if len(i[1]) == 2:
                i[0].insert(len(i[0]) // 2 + 1, '(')
                i[0].insert(len(i[0]) // 2 + 3, ')')
#Для любой возможной оси, находим подходящую
def search(i: list, cuts: list):
    axis = []
    for j in cuts:
        if check_sym(i, len(i), j):
            axis.append([i, j])
    return axis
#Поиск всех многоугольников для n и k
def combinations(n: int, k: int):
    a = '1' * k + '0' * (n - k)
    for i in itertools.product('10', repeat=n):
        if i.count('1') == k:
            yield list(i)
    return
#Поиск всех классов эквивалентностей
def symmetry(n: int, k: int):
    pnt = []
    if n % 2 == 0 and k % 2 == 0:
        pnt = ['00', '11', '']
    elif not n % 2 == 0 and k % 2 == 0:
        pnt = ['0']
    elif n % 2 == 0 and not k % 2 == 0:
        pnt = ['10']
    else:
        pnt = ['1']
    figures = []
    for i in combinations(n, k):
        figures += search(i, pnt)
    draw(figures)
    for i in figures:
        res = ''
        for sym in i[0]:
            res += sym
        print(res)

input = input().split()
n = int(input[0])
k = int(input[1])
symmetry(n, k)
#В скобка () обозначены вершины, являющиеся коцнами осей симметрии
#| - ось, выходящая из стороны многоугольника и приходящая в противоположную