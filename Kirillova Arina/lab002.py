import math

def GenSimpleArr(n : int, k : int):
    return [1] * k + [0] * (n - k)

def GenAllArr(current: str, n: int):
    if (len(current) == n):
        return [[int(t) for t in list(current)]]
    comb = []
    comb += GenAllArr(current + '0', n)
    comb += GenAllArr(current + '1', n)
    return comb

def RemoveEqual(comb: list):
    comb2 = []
    for i in range(len(comb)):
        if comb[i] != None:
            comb2.append(comb[i])
            for j in range(i + 1, len(comb)):
                if (comb[j] != None and Compare(comb[i], comb[j])):
                    comb[j] = None
    return comb2

def RemoveWithOnes(comb: list, k:int):
    comb2 = []
    for i in range(len(comb)):
        n = 0
        for j in range(0, len(comb[i])):
          if (comb[i][j] == 1):
            n += 1
        if n == k:
            comb2.append(comb[i])
    return comb2


def CycleStep(arr : list, step : int):
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[(i + step) % len(arr)])
    return arr2

def Compare(arr1: list, arr2: list):
    for shift in range(len(arr1)):
        flag = True
        for j in range(len(arr1)):
            if (arr1[j] != arr2[j]):
                flag = False
                break
        if flag:
            return True
        arr1 = CycleStep(arr1, 1)
    return False

class Axis:
    def __init__(self, type, index1, index2, clas):
        self.type = type
        self.index1 = index1
        self.index2 = index2
        self.clas = clas

def AxisVertex(comb:list):
    axis = []
    for clas in (comb):
        for start in range(len(clas) // 2):
            flag = True
            for check in range(1, len(clas) // 2):
                if (clas[(start + check)% len(clas)] != clas[start - check]):
                    flag = False
                    break
            if (flag):
                axis.append(Axis("Vertex", start, (start + len(clas) / 2) % len(clas), clas))
    return axis

def AxisEdge(comb:list):
    axis = []
    for clas in (comb):
        for start in range(len(clas) // 2):
            flag = True
            for check in range(1, len(clas) // 2 + 1):
                if (clas[(start + check)% len(clas)] != clas[start - check + 1]):
                    flag = False
                    break
            if (flag):
                axis.append(Axis("Edge", start + 0.5, (start + len(clas) / 2) % len(clas), clas))
    return axis


def AxisVertexEdge(comb:list):
    axis = []
    for clas in (comb):
        for start in range(len(clas)):
            flag = True
            for check in range(1, len(clas) // 2 + 1):
                if (clas[(start + check) % len(clas)] != clas[start - check]):
                    flag = False
                    break
            if (flag):
                axis.append(Axis("VertexEdge", start, (start + len(clas) / 2) % len(clas), clas))
    return axis


def GetAllAxis(comb:list):
    n = len(comb[0])
    ans = []
    if n % 2 == 0:
        ans += AxisVertex(comb)
        ans += AxisEdge(comb)
    else:
        ans += AxisVertexEdge(comb)
    frames = dict()
    n = 0
    for tuples in comb:
        frames[tuple(tuples)] = []
    for axis in ans:
        frames[tuple(axis.clas)].append(axis)
    return frames

if __name__ == '__main__':
    size = 5
    ones = 3
    comb = GenAllArr('', size)
    comb = RemoveEqual(comb)
    comb = RemoveWithOnes(comb, ones)
    print("Number of classes", len(comb))
    Axiss = GetAllAxis(comb)
    for el in Axiss:
      print("Class:", str(el))
      #draw polygon
      n = 1
      for ax in Axiss[el]:
        print(str(n) + ") Type:", ax.type, "index1:", ax.index1, "index2:", ax.index2)
        n += 1
