def FromDec(sys, num, flag = True):
    Symbols = "0123456789ABCDEFGHIJKLMNOPRSTUVWXYZ"
    mod = num % sys
    if num == 0 and flag:
        return "0"
    elif num == 0:
        return ""
    return FromDec(sys, num // sys, False) + Symbols[mod]

def ToDec(sys, num):
    return int(num, sys)

def Kaprekar(sys, num):
    digits = list(num)
    digits.sort()
    minNum = "".join(digits)
    digits.reverse()
    maxNum = "".join(digits)
    return FromDec(sys, ToDec(sys, maxNum) - ToDec(sys, minNum))

def NumberPrepare(sys, num):
    rez = [num]
    while rez.count(num) == 1:
        num = Kaprekar(sys, num)
        rez.append(num)
    return rez

def Research(sys, numOfDigits, file):
    for i in range(sys ** (numOfDigits - 1), sys ** numOfDigits):
        rez = NumberPrepare(sys, FromDec(sys, i))
        file.write("Number: " + FromDec(sys, i) + "\n    radix: " + str(sys) + "\n    number Of Digits: " + str(numOfDigits) + '\t' +
                     "\n    lenth of cykle: " + str(len(rez) - 1 - rez.index(rez[-1])) + "\n    number starting cykle: " + rez[-1] + "\n    steps untill cykle: " 
                        + str(rez.index(rez[-1])) + "\n    sequense kaprekar steps: " + str(rez) + '\n\n\n')

if __name__ == "__main__":
    file = open("result.txt", "w")
    for sys in range(2, 16):
        for dig in range(2, 8):
            
            Research(sys, dig, file)
file.close()
