from itertools import *


n = 6
k = 4
t = 0
def GenerateBitString(n, k):
    # Генерируютя комбинации из блоков единиц
    # Каждый элемент комбинации показывает
    # сколько будет стоять единиц после очередного нуля
    CombinationList = []
    for Combination in map(list, product(range(k + 1), repeat=n-k)):
        NumberOfOne = 0
        for Blok in Combination:
            NumberOfOne += Blok
        if NumberOfOne == k:
            CombinationList.append(Combination)

    BitStringList = []
    for Combination in CombinationList:
        BitString = ""
        for NumOfOne in Combination:
            BitString += "0" + "1" * NumOfOne
        for _ in range(n):
            if BitString in BitStringList:

                break
            BitString = BitString[1:] + BitString[0]
        else:
            BitStringList.append(BitString)



    return BitStringList


def FindSymmetry(BitString):
    n = len(BitString)
    EquivalenceClass = set()
    for _ in range(n):

        if n % 2 == 0:
            if BitString[1:n//2] == BitString[-1:-n//2:-1]:
                EquivalenceClass.add("(" + BitString[0] + ")" + BitString[1:n//2] + "(" + BitString[n//2] + ")" + BitString[n//2 + 1:])

            if BitString[:n//2] == BitString[-1:-n//2 - 1:-1]:
                EquivalenceClass.add(BitString[:n//2] + "|" + BitString[n//2:])

        else:
            if BitString[:n//2] == BitString[-1:-n//2:-1]:
                EquivalenceClass.add(BitString[:n//2] + "(" + BitString[n//2] + ")" + BitString[n//2 + 1:])

        BitString = BitString[1:] + BitString[0]
    return EquivalenceClass

for n in range(3, 10):
    for k in range(1, n):
        print("n=", n, "k=", k)

        BitStringList = GenerateBitString(n, k)
        for BitString in BitStringList:
            EquivalenceClass = FindSymmetry(BitString)
            for Equivalence in EquivalenceClass:
                print(Equivalence)
# BitString = "0010100"
# n = len(BitString)
# print(BitString[:n//2])
# print(BitString[-1: -n//2: -1])
