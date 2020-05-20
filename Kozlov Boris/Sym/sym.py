"""
Примитивная функция, считающая количество 1 в двоичной записи десятичного числа.
"""
def count_ones(number):
    quantity = 0
    while number > 0:
        quantity += number & 1
        number >>= 1
    return quantity


"""
Функция, реализующая циклический сдвиг вправо на заданное количество шагов.
"""
def shift(number, step):
    temp = ''
    while number > 0:
        temp += str(number % 2)
        number //= 2
    number_list = list(reversed(temp))
    for i in range(step):
        number_list.insert(0, number_list.pop())
    return int("".join(number_list), 2)


"""
Функция, выделяющая из множества чисел заданной длины и 
с заданным количеством единиц в двоичной записи подмножество таких чисел,
из которых могут быть получены все другие числа множества путем циклического сдвига.
Сами числа подмножества не могут быть получены друг из друга таким путем.
"""
def create_unique_number_sequences(len, ones):
    answer = []
    full_set = []
    for number in range(2 ** (len - 1), 2 ** len):
        if count_ones(number) == ones and number not in full_set:
            answer.append(number)
        temp = number
        for step in range(1, len):
            full_set.append(temp)
            temp = shift(number, step)
    return answer


"""
Функция, считающая, относительно скольких осей симметрии в правильном многоугольнике, значения в
вершинах которого могут принимать значения 0 или 1, и чьи вершины 
образуют последовательность, являющуюся записью введенного числа в двоичной
системе, подпоследовательности вершин с двух сторон совпадают. Оси симметрии 2n-угольника могут
проходить через противоположные вершины или через середины двух противоположных сторон, в то время
как у (2k+1)-угольника они могут проходить только через вершину и середину противоположной стороны.
"""
def count_axis_in_sequence(number):
    quantity = 0
    temp = ''
    while number > 0:
        temp += str(number % 2)
        number //= 2
    number_list = list(reversed(temp))
    len_list = temp.__len__()
    is_subsequence = 0
    if len_list % 2 == 0:
        sub_len = int((len_list - 2) / 2)
        for i in range(sub_len + 1):
            is_subsequence = 1
            for j in range(1, sub_len + 1):
                if number_list[i - j] != number_list[i + j]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
        sub_len = int(len_list / 2)
        for i in range(sub_len):
            is_subsequence = 1
            for j in range(sub_len):
                if number_list[i - j] != number_list[i + 1 + j]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
    else:
        sub_len = int((len_list - 1) / 2)
        for i in range(len_list):
            is_subsequence = 1
            for j in range(1, sub_len + 1):
                if number_list[(i - j) % len_list] != number_list[(i + j) % len_list]:
                    is_subsequence = 0
                    break
            if is_subsequence == 1:
                quantity += 1
    return quantity


"""
Предполагается, что заданное множество содержит
элементы по крайней мере с 1 единицей в записи.
Если же нет, то, очевидно, что вводимый нуль длины
n образует многоугольник, у которого относительно всех
осей симметрии будет наблюдаться совпадение подпоследовательностей
с обеих сторон.
"""
len = int(input("Enter the sequence's length: "))
num_of_ones = int(input("Enter the number of ones: "))
if len >= 3 and num_of_ones > 0:
    sequences = create_unique_number_sequences(len, num_of_ones)
    for sequence in sequences:
        print(str(bin(sequence)) + " is a unique sequence,")
        print("It has " + str(count_axis_in_sequence(sequence)) + " axis of symmetry overall.\n")
elif len >= 3 and num_of_ones == 0:
    print("0b".ljust(len + 2, '0') + " is the only sequence possible,")
    print("It has " + str(count_axis_in_sequence(2 ** len - 1)) + " axis of symmetry overall.\n")
else:
    print("Incorrect input, please try again.")