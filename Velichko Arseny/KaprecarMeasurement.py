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

def kaprekarMultFunc(listOfDigits, allUsedNums, radix):
    currUsedNums = dict()
    startList = listOfDigits.copy()
    numAsStr = startAsStr = listToStr(startList)
    isCycle = True
    while currUsedNums.get(numAsStr) == None:
        if numAsStr not in allUsedNums:
            allUsedNums.add(numAsStr)
            kaprekarSingleFunc(listOfDigits, radix)
            if listOfDigits < startList:
                isCycle = False
                break
            prevStr = numAsStr
            numAsStr = listToStr(listOfDigits)
            currUsedNums[prevStr] = numAsStr
        else:
            isCycle = False
            break
    allUsedNums.remove(startAsStr)
    if isCycle == True:
        return True, clearCycle(currUsedNums, numAsStr)
    return False, None

def clearCycle(numsDict, cycleBegin):
    cycleList = []
    currStr = cycleBegin
    while numsDict[currStr] != cycleBegin:
        currStr = numsDict[currStr]
        cycleList.append(currStr)
    cycleList.append(cycleBegin)
    return cycleList

def increasePivotList(pivotList):
    i = len(pivotList) - 1
    pivotList[i] += 1
    while i > 0 and pivotList[i] > pivotList[i - 1]:
        pivotList[i] = 0
        i -= 1
        pivotList[i] += 1

def kaprekarMeasurement(digit, radix):
    allUsedNums = set()
    allCycles = []
    pivotList = [0 for i in range(digit)]
    currFirst = 0
    while pivotList[0] < radix:
        if (currFirst < pivotList[0]):
            currFirst = pivotList[0]
            print(currFirst)
        isCycle, cycleList = kaprekarMultFunc(pivotList.copy(), allUsedNums, radix)
        if isCycle:
            allCycles.append(cycleList)
        increasePivotList(pivotList)
    return allCycles

#####main#####
allCycles = kaprekarMeasurement(10, 16)
for i in range(len(allCycles)):
   for j in range(len(allCycles[i])):
       print(allCycles[i][j], end = ' ')
   print()
