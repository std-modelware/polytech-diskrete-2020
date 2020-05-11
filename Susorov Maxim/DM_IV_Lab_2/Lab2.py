import itertools


def GenerateSequences(n: int, k: int):
    """
    Function generates all sequences of length 'n' with 'k' ones,
    excluding the sequences, which can be built by cycle shift
    :param n: length of sequence
    :param k: count of ones
    :return: list(str())
    """
    sequences = list()
    list_of_nums = '1' * k + '0' * (n - k)
    for permutation in itertools.permutations(list_of_nums, n):
        if permutation not in sequences:
            sequences.append(permutation)
    for seq in sequences:
        for i in range(n):
            shifted = CycleShift(seq, i)
            if shifted in sequences and shifted != seq:
                sequences.remove(shifted)
    return sequences


def CycleShift(seq: list, offset: int):
    """
    Function generates cycle shift to left of sequence 'seq' with offset 'offset'
    :param seq: sequence to cycle shift
    :param offset: offset in shifting
    :return: list()
    """
    shifted_seq = seq[offset:] + seq[:offset]
    return shifted_seq


def VertexVertexSymmetry(sequence: list, n: int):
    """
    Function checks symmetry of type, when symmetry axe starts in vertex and ends in vertex
    :param sequence: sequence to check
    :param n: length
    :return: list(bool, list())
    """
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = CycleShift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index):
            if seq[i] != seq[-i]:
                mid_result = False
        if mid_result:
            return [mid_result, seq]
        result = result or mid_result
    return [result, list()]


def VertexEdgeSymmetry(sequence: list, n: int):
    """
    Function checks symmetry of type, when symmetry axe starts in vertex and ends in edge
    :param sequence: sequnce to check
    :param n: length
    :return: list(bool, list())
    """
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = CycleShift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index + 1):
            if seq[i] != seq[-i]:
                mid_result = False
        if mid_result:
            return [mid_result, seq]
        result = result or mid_result
    return [result, list()]


def EdgeEdgeSymmetry(sequence: list, n: int):
    """
    Function checks symmetry of type, when symmetry axe starts in edge and ends in edge
    :param sequence: sequnce to check
    :param n: length
    :return: list(bool, list())
    """
    symmetry_index = n // 2
    result = False
    for offset in range(n):
        seq = CycleShift(sequence, offset)
        mid_result = True
        for i in range(symmetry_index):
            if seq[i] != seq[-i - 1]:
                mid_result = False
        if mid_result:
            return [mid_result, seq]
        result = result or mid_result
    return [result, list()]


def Research(maxN: int):
    """
    Function does research: find count of equivalence classes and symmetry axes of every type of symmetry
    :param maxN:
    :return: none
    """
    for n in range(3, maxN + 1):
        print("--------------------------------------------------------------------------------------")
        print("                             AMOUNT OF ELEMENTS == %d                               " % n)
        print("--------------------------------------------------------------------------------------")
        for k in range(n + 1):
            sequences = GenerateSequences(n, k)
            print("___k___ = %d:" % k, end='')
            print("\tNumber of equivalence classes = %d" % len(sequences))
            if n % 2 == 0:
                vertex_vertex = 0
                edge_edge = 0
                for seq in sequences:
                    if VertexVertexSymmetry(seq, n)[0]:
                        vertex_vertex += 1
                    if EdgeEdgeSymmetry(seq, n)[0]:
                        edge_edge += 1
                print("\t\t\t\tNumber of vertex-vertex symmetry axes = %d" % vertex_vertex)
                print("\t\t\t\tNumber of edge-edge symetry axes = %d" % edge_edge)
            else:
                vertex_edge = 0
                for seq in sequences:
                    if VertexEdgeSymmetry(seq, n)[0]:
                        vertex_edge += 1
                print("\t\t\t\tNumber of vertex-edge symmetry axis = %d" % vertex_edge)


Research(10)