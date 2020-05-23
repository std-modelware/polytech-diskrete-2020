def Gorner(l, r):
    number = 0
    for k in range(len(l)):
        number *= r
        number += int(l[k], r)
    return number

def Converse(number, r):
    alphabet = "0123456789ABCDEF"
    if number < r:
        return alphabet[number]
    return Converse(number // r, r) + alphabet[number % r]

def FillZeros(n, d):
    return '0' * (d - len(n)) + n

def Kaprekar(number, d, r):
    string = str(number)
    string = FillZeros(string, d)
    l = list(string)
    l = [int(ch, r) for ch in l]
    l.sort()
    l = [Converse(num, r) for num in l]
    small = Gorner(l, r)
    l.reverse()
    big = Gorner(l, r)
    return Converse(big - small, r)

def MagicNumbers(d, r):
    supremum = r ** d
    magic = []
    for i in range(supremum):
        num = Converse(i, r)
        kap_num = Kaprekar(num, d, r)
        if num == kap_num:
            magic.append(num)
    return magic

def CycleLength(d, r):
    result = 0
    supremum = r ** d
    for i in range(supremum):
        currentLength = 0
        cycle = []
        i_str = Converse(i, r)
        cycle.append(i_str)
        last = Kaprekar(i_str, d, r)
        while last not in cycle:
            currentLength += 1
            cycle.append(last)
            last = Kaprekar(last, d, r)
        if currentLength > result:
            result = currentLength
    return result

maxNumSys = 10
maxDigits = 5
file = open('kaprekar.csv', 'w')
file.write('"digits","system","cycle length","magic numbers"\n')
for i in range(1, maxDigits + 1):
    for j in range(2, maxNumSys + 1):
        file.write('"%i","%i","%i","%s"\n' % (i, j, CycleLength(i, j), MagicNumbers(i, j)))
file.close()

