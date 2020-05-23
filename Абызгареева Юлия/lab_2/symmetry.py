import itertools


def Create(n: int, k: int):
    sequences = list()
    list_of_nums = '1' * k + '0' * (n - k)
    for permutation in itertools.permutations(list_of_nums, n):
        if permutation not in sequences:
            sequences.append(permutation)
    for seq in sequences:
        for i in range(n):
            shifted = Shift(seq, i)
            if shifted in sequences and shifted != seq:
                sequences.remove(shifted)
    return sequences


def Shift(seq: list, offset: int):
    shifted_seq = seq[offset:] + seq[:offset]
    return shifted_seq


def VertexVertexSymmetry(sequence: list, n: int):
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = Shift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index):
            if seq[i] != seq[-i]:
                mid_result = False
        if mid_result:
            res_seq = str()
            for i in range(n):
                if i == 0 or i == symmetry_index:
                    res_seq += ''.join('(')
                res_seq += ''.join(seq[i])
                if i == 0 or i == symmetry_index:
                    res_seq += ''.join(')')
            return [mid_result, res_seq]
        result = result or mid_result
    return [result, list()]


def VertexEdgeSymmetry(sequence: list, n: int):
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = Shift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index + 1):
            if seq[i] != seq[-i]:
                mid_result = False
        if mid_result:
            res_seq = str()
            for i in range(n):
                if i == 0:
                    res_seq += ''.join('(')
                if i == symmetry_index + 1:
                    res_seq += ''.join('|')
                res_seq += ''.join(seq[i])
                if i == 0:
                    res_seq += ''.join(')')
            return [mid_result, res_seq]
        result = result or mid_result
    return [result, list()]


def EdgeEdgeSymmetry(sequence: list, n: int):
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = Shift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index):
            if seq[i] != seq[-i - 1]:
                mid_result = False
        if mid_result:
            res_seq = str()
            for i in range(n):
                if i == 0 or i == symmetry_index:
                    res_seq += ''.join('|')
                res_seq += ''.join(seq[i])
            return [mid_result, res_seq]
        result = result or mid_result
    return [result, list()]


def Research(maxN: int):
    for n in range(3, maxN + 1):
        print("--------------------------------------------------------------------------------------")
        print("                             AMOUNT OF ELEMENTS == %d                               " % n)
        print("--------------------------------------------------------------------------------------")
        for k in range(n + 1):
            sequences = Create(n, k)
            print("___k___ = %d:" % k, end='')
            print("\tNumber of equivalence classes = %d" % len(sequences))
            if n % 2 == 0:
                vertex_vertex = 0
                edge_edge = 0
                for seq in sequences:
                    if VertexVertexSymmetry(seq, n)[0]:
                        vertex_vertex += 1
                        print("\t\t\t\t%s" % VertexVertexSymmetry(seq, n)[1])
                    if EdgeEdgeSymmetry(seq, n)[0]:
                        edge_edge += 1
                        print("\t\t\t\t%s" % EdgeEdgeSymmetry(seq, n)[1])
                print("\t\t\t\tNumber of vertex-vertex symmetry axes = %d" % vertex_vertex)
                print("\t\t\t\tNumber of edge-edge symetry axes = %d" % edge_edge)
            else:
                vertex_edge = 0
                for seq in sequences:
                    if VertexEdgeSymmetry(seq, n)[0]:
                        vertex_edge += 1
                        print("\t\t\t\t%s" % VertexEdgeSymmetry(seq, n)[1])
                print("\t\t\t\tNumber of vertex-edge symmetry axis = %d" % vertex_edge)


Research(10)
