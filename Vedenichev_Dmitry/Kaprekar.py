def convertBase(num, toBase, fromBase):
    if isinstance(num, str):
        n = int(num, fromBase)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < toBase:
        return alphabet[n]
    else:
        return convertBase(n // toBase, toBase, fromBase) + alphabet[n % toBase]

def OneRun(d, base):#Прогняю все числа для текущих данных
    numberIFind=[];
    for myNumber in range(base**(d-1),base**d):
        result = OneTime(d,base,myNumber)
        if result is not None and result not in numberIFind:
            numberIFind.append(result)
    print(numberIFind)
def OneTime(d, base, myNumber): #Прогоняю одно число
    lowNumber =[];
    highResult = 0;
    lowResult = 0;
    startNumber = convertBase(myNumber, base, 10)
    lowNumber=list(startNumber)
    lowNumber.sort()
    for i in range(len(lowNumber)):
        highResult += (int(str(lowNumber[i]), base) * base ** i);
        lowResult += (int(str(lowNumber[- 1 - i]), base ) * base  ** i);
    result = convertBase(highResult-lowResult, base, 10)
    newNumber=lowNumber
    for i in range(len(newNumber)):
        if i<len(result):
            newNumber[-1-i]= int(result[-1-i])

        else:
            newNumber[-1-i]=0
    newNumber.sort()
    highResult = 0;
    lowResult = 0;
    for i in range(len(newNumber)):
        highResult += (int(str(newNumber[i]), base) * base ** i);
        lowResult += (int(str(newNumber[- 1 - i]), base ) * base  ** i);
    if (int(result,base) == highResult-lowResult):
        return  result
    return

print("Oh, hi, mark");
for i in range(2,7):#Прогон всех начальных условий
    for j in range(2,11):
        print("with base ", j," and ", i, " digits we have :")
        OneRun(i,j)