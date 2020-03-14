def listToStr(listOfDigits):
    resStr = ""
    for i in range(len(listOfDigits)):
        if listOfDigits[i] >= 10:
            resStr += chr(ord('A') + listOfDigits[i] - 10)
        else:
            resStr += str(listOfDigits[i])
    return resStr

def subTwoLists(firstList, secondList, radix):
    length = len(firstList)
    for i in range(length - 1, -1, -1):
        if firstList[i] < secondList[i]:
            firstList[i] += radix
            firstList[i - 1] -= 1
        firstList[i] -= secondList[i]

def kaprekarSingleFunc(sortedList, radix):
    reversedList = sortedList.copy()
    reversedList.reverse()
    subTwoLists(sortedList, reversedList, radix)
    sortedList.sort(reverse = True)

def markNumbers(numsList, allUsedNums, startHeight):
    height = startHeight
    while len(numsList) > 0:
        height = height + 1
        allUsedNums[numsList.pop()] = height
    return height

def kaprekarMultFunc(listOfDigits, allUsedNums, radix):
    currUsedNums = []
    numAsStr = listToStr(listOfDigits)
    isCycle = True
    cycle = None
    height = 0

    while currUsedNums.count(numAsStr) == 0:
        if numAsStr not in allUsedNums:
            currUsedNums.append(numAsStr)
            kaprekarSingleFunc(listOfDigits, radix)
            numAsStr = listToStr(listOfDigits)
            ''' Greatly accelerates the overall calculation process, but makes it impossible to calculate height
            if listOfDigits < startList:
                isCycle = False
                break
            '''
        else:
            isCycle = False
            break
    if isCycle == True:
        currUsedNums.append(numAsStr)
        cycle = eraseCycle(currUsedNums, allUsedNums)
    return cycle, markNumbers(currUsedNums, allUsedNums, allUsedNums[numAsStr])

def eraseCycle(numsList, allUsedNums):
    cycleList = []
    cycleBegin = numsList.pop()
    while numsList[len(numsList) - 1] != cycleBegin:
        currStr = numsList.pop()
        allUsedNums[currStr] = 0
        cycleList.append(currStr)
    allUsedNums[cycleBegin] = 0
    cycleList.append(numsList.pop())
    return cycleList

def increasePivotList(pivotList):
    i = len(pivotList) - 1
    pivotList[i] += 1
    while i > 0 and pivotList[i] > pivotList[i - 1]:
        pivotList[i] = 0
        i -= 1
        pivotList[i] += 1

def kaprekarMeasurement(digit, radix):
    allUsedNums = dict()
    allCycles = []
    pivotList = [0 for i in range(digit)]
    maxHeight = 0
    while pivotList[0] < radix:
        cycleList, height = kaprekarMultFunc(pivotList.copy(), allUsedNums, radix)
        if cycleList != None:
            allCycles.append(cycleList)
        maxHeight = max(maxHeight, height)
        increasePivotList(pivotList)
    return allCycles, maxHeight

#####main#####
recordFile = open('test.txt', 'w')
for digit in range(10, 11):
    for radix in range(10, 11):
        recordFile.write("Digit:" + str(digit) + ' ' + "Radix:" + str(radix) + '\n')
        allCycles, maxHeight = kaprekarMeasurement(digit, radix)
        for i in range(len(allCycles)):
             for j in range(len(allCycles[i])):
                 recordFile.write(allCycles[i][j] + ' ')
             recordFile.write('\n')
        recordFile.write('\n')
        print(digit, radix)
        print(maxHeight)
recordFile.close()