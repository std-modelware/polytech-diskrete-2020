import itertools
from math import pi, cos, sin
from matplotlib import lines
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

R = 1

#генерирует всевозможные последовательности битов
def GenerateSequences(N, K):
    Sequsences = set()
    for seq in itertools.combinations(range(N), K):
        bits = ''
        for i in range(N):
            if i in seq:
                bits += '1'
            else:
                bits += '0'
        Sequsences.add(bits)
    return Sequsences


def symmetricalSelection(Sequences, N):
    result = set()
    if N % 2 == 0:
        for seq in Sequences:
            if seq[1: N//2 : 1] == seq[N - 1 : N//2: -1] and seq[N//2 : N] + seq[0: N//2] + 'a' not in result:
                result.add(seq + 'a')
            if seq[0 : N//2 : 1] == seq[N - 1 : N//2 - 1: -1] and seq[N//2 : N] + seq[0: N//2] + 'b' not in result:
                result.add(seq + 'b')
    else:
        for seq in Sequences:
            if seq[0 : N//2 : 1] == seq[N - 1 : N//2: -1]:
                result.add(seq + 'c')
    return result

def Draw(seq, N):
    plt.axis([-R*1.5, R*1.5, -R*1.5, R*1.5])
    axes = plt.gca()
    axes.set_aspect("equal")
    axes.set_anchor('C')
    coordinates = [[], []]
    alpha = 2 * pi / N
    for i in range(N + 1):
        coordinates[0].append(cos(alpha * i) * R)
        coordinates[1].append(sin(alpha * i) * R)
    for i in range(N):
        plt.text(coordinates[0][i], coordinates[1][i], seq[i])
    lines = mlines.Line2D([coordinates[0]], coordinates[1])
    axes.add_line(lines)
    if seq[-1] == 'a':
        lines = mlines.Line2D([coordinates[0][0], coordinates[0][N//2]],
                              [coordinates[1][0], coordinates[1][N//2]],
                              color='r')
    elif seq[-1] == 'b':
        lines = mlines.Line2D([(coordinates[0][N//2 - 1] + coordinates[0][N//2])/2,
                               (coordinates[0][0] + coordinates[0][N - 1])/2],
                              [(coordinates[1][N // 2 - 1] + coordinates[1][N // 2]) / 2,
                               (coordinates[1][0] + coordinates[1][N - 1]) / 2],
                              color='r')
    elif seq[-1] == 'c':
        lines = mlines.Line2D([coordinates[0][N // 2],
                               (coordinates[0][0] + coordinates[0][N - 1]) / 2],
                              [coordinates[1][N // 2],
                               (coordinates[1][0] + coordinates[1][N - 1]) / 2],
                              color='r')
    axes.add_line(lines)
    plt.title(seq[:N])
    plt.show()



#Main

print("Введите N: ")
N = int(input())
print("Введите K: ")
K = int(input())
AllSequences = GenerateSequences(N, K)
SymSequences = symmetricalSelection(AllSequences, N)


print('Число классов эквивалентности с разными осями симметрии:', len(SymSequences))
for seq in SymSequences:
    Draw(seq, N)
