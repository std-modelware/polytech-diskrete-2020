from itertools import *

def generateAllPermutations(n, k):
    AllPerm = set()
    for i in permutations('0' * (n - k) + '1' * k):
        AllPerm.add(''.join(map(str, i)))
    #print(AllPerm)
    myComb = []
    for comb in AllPerm:
        #print(comb)
        for _ in range(n):
            #print(comb)
            if comb in myComb:
                break
            comb = comb[1:] + comb[0]
        else:
            myComb.append(comb)
    return myComb

def defineSymmetry(Comb):
    SymComb = set()
    n = len(Comb)
    for _ in range(n):
        if n % 2 == 1:
            if Comb[:n//2] == Comb[-1:-n//2:-1]:
                SymComb.add(Comb[:n//2] + "(" + Comb[n//2] + ")" + Comb[n//2 + 1:])
        else:
            if Comb[1:n//2] == Comb[-1:-n//2:-1]:
                SymComb.add("(" + Comb[0] + ")" + Comb[1:n//2] + "(" + Comb[n//2] + ")" + Comb[n//2 + 1:])
            if Comb[:n//2] == Comb[-1:-n//2 - 1:-1]:
                SymComb.add(Comb[:n//2] + "|" + Comb[n//2:])
        Comb = Comb[1:] + Comb[0]
    return SymComb

def main():
    for n in range(3, 11):
        print('Количество вершин = ', n)
        for k in range(1, n):
            print('  Количество единиц = ', k)
            permutations = generateAllPermutations(n, k)
            for comb in permutations:
                SymComb = defineSymmetry(comb)
                if len(SymComb) != 0:
                    for i in SymComb:
                        print('\t', i)

main()
