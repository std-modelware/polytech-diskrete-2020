def Conv (number, base):
    newNum=[]
    if number==0:
        newNum.append(0)
    else:
        while number>=0:
            newNum.append(number%base)
            number //=base
    newNum.reverse()
    return newNum

def Number(numberList, base):
    n=len(numberList)
    num=0
    p=0;
    for i in range(n-1, -1, -1):
        num=num+numberList[i]*(base**p)
        p=p+1
    return num

magicNumber = []
usedNumber = []

# Добавление нужного количества нулей в массив
def AddZeroes (list, n, discharge):
    tmp = discharge - n
    i = 0
    while i < tmp:
        list.append(0)
        i = i + 1

def Subtraction (a, b, base):
    A=Number(a, base)
    B=Number(b, base)
    c=B-A
    result=Conv(c,base)
    return result

def kaprekar(number, discharge, base):
    list_of_digits = number
    list_of_digits1 = list_of_digits
    n = len(list_of_digits)
    if n < discharge:
        AddZeroes(list_of_digits, n, discharge)
    #list_of_digits.sort()
    min = sorted(list_of_digits)
    max = sorted(list_of_digits1, reverse=True)
    delta = Subtraction(min, max, base)
    n = len(delta)
    if n < discharge:
        AddZeroes(delta, n, discharge)
    delta.sort()
    if delta == min:
        delt = Number(delta, base)
        if delt not in magicNumber:
            magicNumber.append(delt)
    return Subtraction(min, max, base)

def Max (a, b):
    if a>b:
        return a
    else:
        return b

for base in range (2,11):
    for discharge in range (2,7):
        max = 0
        for number in range (0, base**discharge):
            maxLenght = 0
            numberList = Conv(number, base)
            while True:
                # print(number, "-> " , end=" ")
                numberList = kaprekar(numberList, discharge, base)
                maxLenght = maxLenght + 1
                numberChange=Number(numberList, base)
                if (numberChange in magicNumber) or (numberChange in usedNumber):
                    # print(number);
                    max=Max(max, maxLenght)
                    break
                usedNumber.append(numberChange)
        print('Система счисления = ', base, end=' ')
        print('Разряд = ', discharge, end=' ')
        print('Максимальная длина = ', max, end=':')
        for i in range(len(magicNumber)):
            magicNumberList=Conv(magicNumber[i], base)
            magicNumberString=''.join(map(str,magicNumberList))
            print(magicNumberString, end=' ')
        print()
        magicNumber = [0]
        usedNumber = []


nd(number)
