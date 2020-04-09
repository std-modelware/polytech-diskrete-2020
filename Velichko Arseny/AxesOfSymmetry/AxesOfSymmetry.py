import matplotlib.pyplot as plt
import math

def buildNumbers(allSpaceLists, digit):
    allNums = [];
    for spaceList in allSpaceLists:
        currNum = [];
        for space in spaceList:
            i = 0;
            for i in range(space):
                currNum.append(0);
            if i < digit - 1:
                currNum.append(1);
        allNums.append(currNum);
    return allNums;

def defineAxes(allNums):
    axesList = [];
    for num in allNums:
        axesList.append([]);
        startLeft = -1;
        startRight = 1;
        for j in range(len(num)):
            left = startLeft;
            right = startRight;
            isSymmetry = True;
            for k in range(len(num) // 2):
                if left < 0:
                    left = len(num) - 1;
                if right >= len(num):
                    right = 0;
                if num[left] != num[right]:
                    isSymmetry = False;
                    break;
                left -= 1;
                right += 1;

            if isSymmetry == True:
                axesList[len(axesList) - 1].append((startLeft + startRight) / 2);
            if j % 2 == 0:
                startLeft += 1;
            else:
                startRight += 1;
    return axesList;

def drawAxes(allNums, axesList):
    for i in range(len(allNums)):
        step = 2 * math.pi / len(allNums[i]);

        for j in range(len(allNums[i])):
            xCoord = math.sin(step * j);
            yCoord = math.cos(step * j);
            if allNums[i][j] == 0:
                plt.scatter(xCoord, yCoord, facecolors = 'none', edgecolors = 'b');
            else:
                plt.scatter(xCoord, yCoord, facecolors = 'b');

        for num in axesList[i]:
            xCoord1 = math.sin(step * num);
            yCoord1 = math.cos(step * num);
            xCoord2 = math.sin(step * (num + len(allNums[i]) / 2));
            yCoord2 = math.cos(step * (num + len(allNums[i]) / 2));
            plt.plot([xCoord1, xCoord2], [yCoord1, yCoord2], '--');
        plt.show();

def cycleCheck(number, startIndex):
    j = 0;
    for i in range(startIndex, len(number)):
        if (number[i] != number[j]):
            return False;
        j += 1;
    return True;

def IterateCurrMax(spaceList, reqSum, depth, allSpaceLists, checkIndex):
    if depth > 0:
        upperBound = min(spaceList[0], reqSum);
        for num in range(upperBound, -1, -1):
            nextCheckIndex = checkIndex;
            if num > spaceList[checkIndex]:
                continue;
            elif num < spaceList[checkIndex]:
                nextCheckIndex = 0;
            else:
                nextCheckIndex += 1;

            nextSpaceList = spaceList.copy();
            nextSpaceList.append(num);
            IterateCurrMax(nextSpaceList, reqSum - num, depth - 1, allSpaceLists, nextCheckIndex);
    elif reqSum <= spaceList[checkIndex]:
        spaceList.append(reqSum);

        if reqSum < spaceList[checkIndex]:
            checkIndex = 0;
        else:
            checkIndex += 1;

        if checkIndex == 0 or cycleCheck(spaceList, checkIndex):
            allSpaceLists.append(spaceList);

def IterateAllSpaces(digit, onesNumber):
    reqSum = digit - onesNumber;
    allSpaceLists = [];
    for num in range(reqSum, -1, -1):
        currList = [];
        checkIndex = 0;
        currList.append(num);
        if onesNumber >= 2:
            IterateCurrMax(currList, reqSum - num, onesNumber - 2, allSpaceLists, checkIndex);
        elif num == reqSum:
            allSpaceLists.append(currList);
    return allSpaceLists;

print("Enter number of digits: ");
digit = int(input());
print("Enter number of ones: ");
onesN = int(input())
allSpaceLists = IterateAllSpaces(digit, onesN);
allNums = buildNumbers(allSpaceLists, digit);
axesList = defineAxes(allNums);
drawAxes(allNums, axesList);
