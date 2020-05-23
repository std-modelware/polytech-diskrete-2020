from math import factorial
import itertools

def createArray(arrayLen, onesCount):
    ones = [1] * onesCount
    zeros = [0] * (arrayLen-onesCount)
    array = zeros + ones
    return array
    
def moveRight(array):
    newArray = array[-1:] + array[: -1]
    return newArray

def is_equal(arr1, arr2):
    buf = arr1
    for i in range(len(arr1)):
        buf = moveRight(buf)
        if (arr2 == buf):
            return True
    return False

def allCombArrays(origArray):
    posibleArrays = list()
    added_bool = False #есть ли уже в списке данная строка
    allCombs = itertools.permutations(origArray) #
    for array in allCombs:
        added_bool = False
        for arr in posibleArrays:
            if is_equal(list(arr), list(array)):
                added_bool = True
                break
        if not added_bool:
            posibleArrays.append(array)
    return posibleArrays

def checkSymmetry(array):
    symArrays = list() #записывает индексы симметрии с типом симметрии
    length = len(array)
    midIndex = length // 2
    arrayBuf = array
    if length % 2 == 0:
        for shift in range(midIndex): #проверка палиндромности половин
            if arrayBuf[0:midIndex - 1] == arrayBuf[length - 2:midIndex - 1:-1]:
                symArrays.append([shift, "points"])
            if arrayBuf[0:midIndex] == arrayBuf[length - 1:midIndex - 1:-1]:
                symArrays.append([shift, "lines"])
            arrayBuf = moveRight(arrayBuf)
    else:
        for shift in range(length): #проверка полной палиндромности(в случае нахождения в середине точки симметрий)
            if arrayBuf == arrayBuf[::-1]:
                symArrays.append([length - shift - 1, "mixed"])
            arrayBuf = moveRight(arrayBuf)
    return symArrays

def printSymArray(array):
    symArrays = checkSymmetry(array)
    for symArray in symArrays:
        string = ''
        pointOfSym = symArray[0]
        symmetryType = symArray[1]
        secondPoint = (pointOfSym + len(array) // 2) % len(array) #в четных случаях
        if symmetryType == "lines": #между вершинами палочка
            for i in range(len(array)):
                point = array[i]
                if i is pointOfSym or i is secondPoint:
                    string += "|"
                string += str(point)
        if symmetryType == "points": #вершину в скобочки
            secondPoint = (pointOfSym + len(array) // 2) % len(array)
            for i in range(len(array)):
                point = array[i]
                if i is pointOfSym or i is secondPoint:
                    string += '(' + str(point) + ')'
                else:
                    string += str(point)
        if symmetryType == "mixed": #вершину в скобочки и в противоположной стороне палочка
            secondPoint = (pointOfSym + 1 + len(array) // 2) % len(array) #в этом случае точка высчитывается по другому
            for i in range(len(array)):
                point = array[i]
                if i is secondPoint:
                    string += '(' + str(point) + ')'
                else:
                    string += str(point)
                    if i is pointOfSym:
                        string += "|"
        print(string)

def main(length, onesCount):
    combinations = allCombArrays(createArray(length, onesCount))
    for array in combinations:
        printSymArray(array)

length = int(input("Введите длину строки"))
onesCount = int(input("Введите количество единиц"))
main(length, onesCount)
