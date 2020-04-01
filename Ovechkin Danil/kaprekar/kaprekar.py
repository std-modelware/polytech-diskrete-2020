def NumberToNumerals(number, d, r):
    result = []
    n = number
    for i in range(d):
        n, tmp = divmod(n, r)
        result.append(tmp)
    return result
def NumeralsToNumber(numerals, r):
    num = 0
    numerals.reverse()
    for i in range(len(numerals)):
        num += numerals[i] * r ** i
    return num
def kaprekar(number, r, d):
    Numerals = NumberToNumerals(number, d, r)
    Numerals.sort()
    min = NumeralsToNumber(Numerals, r)
    Numerals.sort(reverse=True)
    max = NumeralsToNumber(Numerals, r)
    return max - min
def FindConstantsAndCycles(r, d):
    NewNum = 0
    ListConstants = list()
    ListNums = list()
    n = 10 ** d
    length = 0
    MaxLength = 0
    for i in range(n):
        while(True):
            NewNum = kaprekar(i, r, d)
            if NewNum == i:
                if NewNum in ListConstants:
                    break
                ListConstants.append(NewNum)
                break
            elif NewNum in ListNums:
                break
            ListNums.append(NewNum)
            i = NewNum
            length = length + 1
        MaxLength = max(MaxLength, length)
        length = 0
    return ListConstants, MaxLength
def ChangeNumeralSystem(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return ChangeNumeralSystem(n // to_base, to_base) + alphabet[n % to_base]
def Research(file):
    for r in range(2, 11):
        for d in range(2, 7):
            ListConstants, MaxLength = FindConstantsAndCycles(r, d)
            for i in range(len(ListConstants)):
                ListConstants[i] = ChangeNumeralSystem(ListConstants[i], r, 10)
            file.write("Radix: " + str(r) + "\t" + "d: " + str(d) + "\t" + "List of nums: " + str(ListConstants) + "\n\t\t\t" + "Max length: " + str(MaxLength) + "\n")
            
file = open("research.txt", "w")
Research(file)
file.close()
