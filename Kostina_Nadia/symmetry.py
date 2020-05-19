import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Генерирует циклические последовательности с p нулями и q единицами
def cyclic_seq(p, q):
    if p + q == 1:
        return {'0' * p + '1' * q}

    n = p + q
    seq = [{'0', '1'}]
    res = set()

    while seq[-1]:
        cur = seq[-1]
        nxt = []
        for s in cur:

            for k in range(2, n // len(s) + 1):
                nxt.append(k * s)

            for i, ch in enumerate(s):
                if ch == '0':
                    nxt.append(s + s[:i] + '1')

        seq.append(set())

        for s in nxt:
            zeros = sum(ch == '0' for ch in s)
            ones = sum(ch == '1' for ch in s)
            if len(s) > n:
                continue

            if zeros == p and ones == q:
                res.add(s)
            elif zeros <= p and ones <= q:
                seq[-1].add(s)

    return res


def vertex_sym(s, i):
    left = s + s[:i]
    right = s[i + 1:] + s
    zp = zip(left[::-1], right)
    a, b = zip(*zp)
    return a == b


def edge_sym(s, i, after_index=False):

    if after_index:
        if i == len(s) - 1:
            i = 0
        else:
            i += 1

    left = s + s[:i]
    right = s[i:] + s
    zp = zip(left[::-1], right)
    a, b = zip(*zp)
    return a == b


# Количество симметрий
def symmetry(s):
    res = 0
    n = len(s)

    # Вершина ребро
    class1 = []
    # Вершина вершина
    class2 = []
    # Ребро ребро
    class3 = []

    if n % 2 == 1:
        for i, ch in enumerate(s):
            if vertex_sym(s, i):
                res += 1
                j = (i + n // 2 + 1) % n
                if j < i:
                    class1.append(s[:j] + '|' + s[j:i] + '(' + ch + ')' + s[i + 1:])
                else:
                    class1.append(s[:i] + '(' + ch + ')' + s[i + 1: j] + '|' + s[j:])

    else:
        for i in range(n//2):

            i1 = (i + n // 2) % n
            i2 = i

            if i1 > i2:
                i1, i2 = i2, i1

            if vertex_sym(s, i):
                res += 1
                class2.append(s[:i1] + '(' + s[i1] + ')' + s[i1 + 1:i2] + '(' + s[i2] + ')' + s[i2 + 1:])

            if edge_sym(s, i):
                res += 1
                class3.append(s[:i1] + '|' + s[i1:i2] + '|' + s[i2:])

    return res, class1, class2, class3


# Рисует последовательность вместе с ее осями симметрии
def draw(s):
    n = len(s)
    alpha = np.linspace(0, 2 * np.pi, n, endpoint=False)
    R = 12

    # Рисует саму последовательность в виде ожерелья
    plt.figure(figsize=(5, 5))
    for a, ch in zip(alpha, s):
        th = np.linspace(0, 2 * np.pi, 100)
        x = np.cos(th) + np.sin(a) * R
        y = np.sin(th) + np.cos(a) * R
        if ch == '1':
            color = 'darkslategrey'
        else:
            color = 'lightsteelblue'
        plt.plot([R * np.sin(a) * np.ones_like(x),  x], [R * np.cos(a) * np.ones_like(y), y], color=color)

    # Рисует оси
    for i in range(n):
        left, right = s + s[:i], s[i + 1:] + s
        zp = zip(left[::-1], right)
        a, b = zip(*zp)
        if a == b:
            beta = 2 * np.pi / n * i
            plt.plot([0,  R * np.sin(beta)], [0,  R * np.cos(beta)], color='green', lw=2)
            if n % 2 == 1:
                plt.plot([0, -R * np.sin(beta)], [0, -R * np.cos(beta)], color='green', lw=2)
            print(i)

    if n % 2 == 0:
        for i in range(n):
            left, right = s + s[:i], s[i:] + s
            zp = zip(left[::-1], right)
            a, b = zip(*zp)
            if a == b:
                beta = 2 * np.pi / n * (i - 0.5)
                plt.plot([0, R * np.sin(beta)], [0, R * np.cos(beta)], color='darkorange', lw=2)

    plt.show()


columns = ['#digits', '#ones', '#symm', '#class1', '#class2', '#class3', 'class1', 'class2', 'class3']
df = pd.DataFrame(columns=columns)
for k in range(3, 10):
    for ones in range(0, k + 1):
        zeros = k - ones
        result = 0
        class1, class2, class3 = [], [], []
        for s in cyclic_seq(zeros, ones):
            ans = symmetry(s)
            #print(ans[0])
            result += ans[0]
            class1 += ans[1]
            class2 += ans[2]
            class3 += ans[3]
        values = [k, ones, result, len(class1), len(class2), len(class3), class1, class2, class3]

        df = df.append(dict(zip(columns, values)), ignore_index=True)


df.to_csv(r'./symmetries.csv', mode='w')
