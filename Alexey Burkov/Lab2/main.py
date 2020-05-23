def next_sequence(sequence):
    ones_skipped = 0
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] == 1:
            if (i != len(sequence) - 1) and (sequence[i + 1] == 0):
                sequence[i] = 0
                sequence[i + 1] = 1
                for j in range(i + 2, len(sequence)):
                    if ones_skipped:
                        sequence[j] = 1
                        ones_skipped -= 1
                    else:
                        sequence[j] = 0
                return sequence
            else:
                ones_skipped += 1
    return []


def cyclic_shift(sequence):
    last = sequence[len(sequence) - 1]
    for i in range(len(sequence) - 1, 0, -1):
        sequence[i] = sequence[i - 1]
    sequence[0] = last
    return sequence


def find_different_sequences(length, ones_quantity):
    sequences = []
    seq = [0 for i in range(length)]
    for i in range(ones_quantity):
        seq[i] = 1
    while len(seq):
        different = True
        s1 = seq.copy()
        for i in range(length):
            if s1 in sequences:
                different = False
                break
            s1 = cyclic_shift(s1)
        if different:
            sequences.append(seq.copy())
        seq = next_sequence(seq)
    return sequences


def check_axis(sequence, axis):
    index1 = axis[0] // 2
    index2 = index1 - 1
    if axis[0] % 2:
        index2 += 1
    for i in range(len(sequence) // 2 + 1):
        if sequence[(index1 + i) % len(sequence)] != sequence[(index2 - i) % len(sequence)]:
            return False
    return True


def find_symmetry(sequence):
    symmetry_axis = []
    length = len(sequence)
    # 2 числа однозначно определяют места пересечения осью многоугольника
    # axis//2 - номер вершины, axis%2 указание на то, вершина это или ребро ведущее к этой вершине
    for i in range(length):
        if check_axis(sequence, [i, i + length]):
            symmetry_axis.append([i, i + length])
    return symmetry_axis


n = 8
k = 4
seq = find_different_sequences(n, k)
for s in seq:
    print("".join(map(str, s)), ':')
    axis = find_symmetry(s)
    if not len(axis):
        print("No symmetry\n")
        continue
    counter = 1
    for a in axis:
        print(counter, ') ', sep='', end='')
        counter += 1
        for i in range(a[0] // 2):
            print(s[i], sep='', end='')
        if a[0] % 2:
            print('[', s[a[0] // 2], ']', sep='', end='')
        else:
            print('|', s[a[0] // 2], sep='', end='')
        for i in range(a[0] // 2 + 1, a[1] // 2):
            print(s[i], sep='', end='')
        if a[1] % 2:
            print('[', s[a[1] // 2], ']', sep='', end='')
        else:
            print('|', s[a[1] // 2], sep='', end='')
        for i in range(a[1] // 2 + 1, n):
            print(s[i], sep='', end='')
        print()
    print()
