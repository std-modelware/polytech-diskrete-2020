import numpy as np

alphabet = []
colors = np.full(26, 0)

def checkLetter(letter, graph):
    if colors[letter] == 2:  # point is black
        return True
    if colors[letter] == 1:  # point is gray
        return False
    colors[letter] = 1;  # point was white and now gray
    if checkNeighbours(letter, graph):
        colors[letter] = 2;
        alphabet.append(letter)
        return True
    return False


def checkNeighbours(letter, graph):
    for i in range(0, len(graph[letter])):
        if not checkLetter(ord(graph[letter][i]) - ord('a'), graph):
            return False
    return True


def alienOrder():

    words = input("Введите слова через пробел\n")
    words = words.lower().split()
    wordCount = len(words)


    meetedWord = np.full(26, False)

    graph = np.full(26, "")  # двумерный массив
    for i in range(0, len(words)):  # пробег по словам
        for j in range(0, len(words[i])):  # пробег по буквам
            meetedWord[ord(words[i][j]) - ord('a')] = True

    for i in range(0, len(words) - 1):
        j = 0;
        while j < min(len(words[i]), len(words[i + 1])) and words[i][j] == words[i + 1][j]:
            j += 1
        graph[ord(words[i + 1][j]) - ord('a')] += words[i][j]

    for i in range(0, 25):
        if meetedWord[i]:
            if not checkLetter(i, graph):
                print("Обнаружен цикл. Невозможно построить алфавит")
                return False

    alienAlphabet = ""
    for i in range(0, len(alphabet)):
        alienAlphabet += chr(alphabet[i] + ord('a'))
    print(alienAlphabet)


alienOrder()

#Решение задачи Alien Dictionary с использованием графов и поиска в глубину
#Условия задачи: дано упорядоченное в лексикографическом порядке множество английских слов.
#                нужно вывести алфавит по которому построен этот порядок.
#                в случаях неопределённости порядка, ответ выводится на основе английского алфавита
#                в случаях зацикленности графов, выводится уведомление.
# Примеры:
#  input: abc bca cab
#  output: abc

#  input: wrt wrf er ett rftt
#  output: wertf

#  input: abc bca aab
#  output: Обнаружен цикл. Невозможно построить алфавит
