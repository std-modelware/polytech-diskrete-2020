def DecimalToAny(base, num, flag = True):
    mods = "0123456789ABCDEFGHIJKLMNOPRSTUVWXYZ"
    mod = num % base
    if num == 0 and flag:
        return "0"
    elif num == 0:
        return ""
    return DecimalToAny(base, num // base, False) + mods[mod]

def AnyToDecimal(base, num):
    return int(num, base)

def Kaprekar(base, num):
    digits = list(num)
    digits.sort()
    minNum = "".join(digits)
    digits.reverse()
    maxNum = "".join(digits)
    return DecimalToAny(base, AnyToDecimal(base, maxNum) - AnyToDecimal(base, minNum))

def ProcessNumber(base, num):
    rez = [num]
    while rez.count(num) == 1:
        num = Kaprekar(base, num)
        rez.append(num)
    return rez

def Research(base, numOfDigits, file):
    for i in range(base ** (numOfDigits - 1), base ** numOfDigits):
        rez = ProcessNumber(base, DecimalToAny(base, i))
        file.write(DecimalToAny(base, i) + '\t' + str(base) + '\t' + str(numOfDigits) + '\t' + 
                   str(len(rez) - 1 - rez.index(rez[-1])) + '\t' + rez[-1] + '\t'
                  + str(rez.index(rez[-1])) + '\t' + str(rez) + '\n')

if __name__ == "__main__":
    file = open("a.tsv", "w")
    file.write("number" + '\t' + "radix" + '\t' + "number Of Digits" + '\t' + 
                   "lenth of cykle" + '\t' + "number starting cykle" + '\t'
                  + "steps untill cykle" + '\t' + "sequense kaprekar steps" + '\n')

    for base in range(2, 16):
        for dig in range(2, 8):
            Research(base, dig, file)
    file.close()

