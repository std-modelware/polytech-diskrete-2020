import itertools
import matplotlib.pyplot as plot
import numpy
import random

# оси симметрии для последовательностей с длинной массива равной четному числу
def SymmetryEvenNumb(seq, n):
    axes = list()
    N = n // 2
    for i in range(N):
        if seq[N - 1::-1] == seq[N:]:
            str = seq[:N] + '|' + seq[N:]
            axes.append(str)
        if seq[N - 1::-1] == seq[N + 1:]:
            str = '(' + seq[0] + ')' + seq[1:N] + '(' + seq[N] + ')' + seq[N + 1:]
            axes.append(str)
        seq = seq[-1] + seq[:-1]
    return axes


# оси симметрии для последовательностей с длиной массива равной нечетному числу
def SymmetryOddNumb(seq, n):
    axes = list()
    N = n // 2
    for i in range(n):
        if seq[N - 1::-1] == seq[N + 1:]:
            str = seq[:N] + '(' + seq[N] + ')' + seq[N + 1:]
            axes.append(str)
        seq = seq[-1] + seq[:-1]
    return axes


# убрать элементы, которые получаются циклическим сдвигом
def removeShift(seq, n):
    k = 0
    l = len(seq)
    seq1 = list()
    for num in seq:
        seq1.append(num)
        for i in range(len(seq)):
            num = num[i:] + num[:i]
            if num in seq:
                seq.remove(num)
    return seq1


# последовательность длинны n с количеством единиц равным k
def sequence(n, k):
    l = list()
    l = k * '1' + (n - k) * '0'
    seq = list()
    for perm in itertools.permutations(l, n):
        tmp = ''.join(perm)
        if tmp not in seq:
            seq.append(tmp)
    seq1 = removeShift(seq, n)
    return seq1

#рисование многоугольника и его осей симметрии
def drawPolygone(seq, n, R, par, axes):
    point = list()
    x_0 = list()
    y_0 = list()
    x_1 = list()
    y_1 = list()
    x = list()
    y = list()
    tmp = [0, 0]
    count = random.randint(1, 5)
    plot.figure(count)
    for i in range(n + 1):
        if (i != n):
            if seq[i] == '0':
                x_0.append(R * numpy.cos(2 * numpy.pi * i / n))
                y_0.append(R * numpy.sin(2 * numpy.pi * i / n))
            if seq[i] == '1':
                x_1.append(R * numpy.cos(2 * numpy.pi * i / n))
                y_1.append(R * numpy.sin(2 * numpy.pi * i / n))
        x.append(R * numpy.cos(2 * numpy.pi * i / n))
        y.append(R * numpy.sin(2 * numpy.pi * i / n))
    plot.plot(x, y, 'b', linewidth=2)
    plot.scatter(x_0, y_0, edgecolors='black', c='black')
    plot.scatter(x_1, y_1, edgecolors='red', c='red')
    if par==1:
        for i in range(4):
            axesX=list()
            axesY=list()
            axesX.append(x[i])
            axesX.append(x[i + n//2])
            axesY.append(y[i])
            axesY.append(y[i + n // 2])
            plot.plot(axesX, axesY, 'g', linewidth=1)
    elif par==2:
        N=n//2
        for i in range(0, 3, 2):
            axesX=list()
            axesY=list()
            x1=(x[i+n//2]-x[i+n//2-1])/2+x[i+n//2-1]
            y1=(y[i+n//2]-y[i+n//2-1])/2+y[i+n//2-1]
            axesX.append(x1)
            axesX.append(-x1)
            axesY.append(y1)
            axesY.append(-y1)
            plot.plot(axesX, axesY, 'g', linewidth=1)
    plot.show()


f = open('lab2Result.txt', "w")

#поиск осей симметрии
def symmetry(seq, n):
    sym = 0
    for num in seq:
        if n % 2 == 0:
            axes = SymmetryEvenNumb(num, n)
        else:
            axes = SymmetryOddNumb(num, n)
        if axes != []:
            sym = sym + len(axes)
            for a in axes:
                f.write(a + ' ' + '\n')
    return sym


# запись результатов эксперимента в файл
for n in range(6, 11):
    for k in range(3, n // 2 + 1 + 1):
        seq = sequence(n, k)
        f.write(str(n) + ' ' + str(k) + '\n')
        k = len(seq)
        f.write('Количество бинарных последовательностей: ' + str(k) + '\n')
        sym = symmetry(seq, n)
        f.write('Количество осей симметрии: ' + str(sym) + '\n' + '\n')

# визуализация для последовательности 10101010
seq = '10101010'
n = 8
R = 6
axes = SymmetryEvenNumb(seq, n)
drawPolygone(seq, n, R, 1, axes)

#визуализация для последовательности 01100110
seq = '01100110'
n = 8
R = 6
axes = SymmetryEvenNumb(seq, n)
drawPolygone(seq, n, R, 2, axes)

