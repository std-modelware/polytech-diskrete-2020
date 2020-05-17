mt_chain = []
used = []


# создание списка смежности
def generate_adjency_matrix():
    with open(r'in1.txt', 'r') as file:
        len_x, len_y = next(file).split(' ')
        len_x = int(len_x)
        len_y = int(len_y)
        if len_x > len_y:
            return None
        next(file)
        adj_array = []
        s = next(file)
        while True:
            for e in s.split(' '):
                adj_array.append(int(e))
            try:
                s = next(file)
            except StopIteration:
                break
        header = adj_array[:len_x + 1]
        bias_adj_ranges = [header[i + 1] - header[i] for i in range(len(header) - 1)]
        adj_mat = [[0 for j in range(len_y)] for i in range(len_x)]
        for head_index in range(len(header) - 1):
            adj_mat[head_index] = [adj_array[header[head_index] - 1 + bias] - 1 for bias in range(bias_adj_ranges[head_index])]
        return adj_mat, len_y


def write_result(lst):
    with open('out.txt', 'w') as file:
        file.write(lst)


# составление чередующейся цепи через обход в глубину
def kuhn(adj_mat, x):
    if used[x]:
        return False
    used[x] = True
    for y in adj_mat[x]:
        if (mt_chain[y] == -1) or (kuhn(adj_mat, mt_chain[y])):
            mt_chain[y] = x
            return True
    return False


def find_matching(adj_mat, len_y):
    global used
    global mt_chain
    mt_chain = [-1 for i in range(len_y)]
    for i in range(len(adj_mat)):
        used = [False for i in range(len(adj_mat))]
        kuhn(adj_mat, i)
    if not (-1 in mt_chain):
        return 'Y\n' + ' '.join([str(e + 1) for e in mt_chain])
    else:
        return 'N\n' + str(mt_chain.index(-1) + 1)


def main():
    adj_mat = None
    try:
        adj_mat, len_y = generate_adjency_matrix()
    except:
        write_result('N\n1')
        adj_mat = None
    if adj_mat:
        write_result(find_matching(adj_mat, len_y))


if __name__ == '__main__':
    main()
