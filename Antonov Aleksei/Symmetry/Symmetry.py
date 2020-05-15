from itertools import permutations


def is_same(seq_1: list, seq_2: list):
    for shift in range(len(seq_1)):
        if seq_2 == (seq_1[-shift:] + seq_1[: -shift]):
            return True
    return False


def generate_sequences(ones_num: int, digits_num: int):
    sequences = list()
    zeros_num = digits_num - ones_num
    for sequence in permutations([0] * zeros_num + [1] * ones_num):
        is_add = True
        for seq in sequences:
            if is_same(list(sequence), list(seq)):
                is_add = False
                break
        if is_add:
            sequences.append(sequence)
    return sequences


def find_axes(sequence: list):
    axes = list()
    len_ = len(sequence)
    seq = sequence
    mid = len_ // 2
    if len_ % 2 == 0:
        for shift in range(mid):
            if seq[1:mid] == seq[:mid:-1]:
                axes.append([shift, "nodes"])
            if seq[:mid] == seq[:mid - 1:-1]:
                axes.append([shift, "middles"])
            seq = seq[-1:] + seq[: -1]
    else:
        for shift in range(len_):
            if seq == seq[::-1]:
                axes.append([len_ - shift - 1, "mid_node"])
            seq = seq[-1:] + seq[: -1]
    return axes


def print_axes(sequence: list):
    axis_ = find_axes(sequence)
    for node_ in axis_:
        type_ = node_[1]
        node_1 = node_[0]
        with open("result.csv", 'a') as file:
            if type_ == "nodes":
                node_2 = (node_1 + len(sequence) // 2) % len(sequence)
                for i in range(len(sequence)):
                    node = sequence[i]
                    if i is node_1 or i is node_2:
                        file.write(f"({node})")
                    else:
                        file.write(f"{node}")
                file.write(" ")
            if type_ == "middles":
                node_2 = (node_1 + len(sequence) // 2) % len(sequence)
                for i in range(len(sequence)):
                    node = sequence[i]
                    if i is node_1 or i is node_2:
                        file.write("|")
                    file.write(f"{node}")
                file.write(" ")
            if type_ == "mid_node":
                node_2 = (node_1 + 1 + len(sequence) // 2) % len(sequence)
                for i in range(len(sequence)):
                    node = sequence[i]
                    if i is node_2:
                        file.write(f'({node})')
                    else:
                        file.write(f"{node}")
                        if i is node_1:
                            file.write("|")
                file.write(" ")


with open("result.csv", 'w') as file:
    file.write("Num of digits,Num of ones,Classes\n")
for n in range(3, 10):
    for k in range(n + 1):
        combinations = generate_sequences(k, n)
        with open("result.csv", 'a') as file:
            file.write(f"n={n},k = {k},")
        for sequence_ in combinations:
            print_axes(sequence_)
        with open("result.csv", 'a') as file:
            file.write(f"\n")
