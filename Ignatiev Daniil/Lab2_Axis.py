import itertools


def SideCheck(List: list):
    for i in range(0, len(List)//2):
        if List[i] != List[-(i+1)]:
            return False
    return True


def AncleCheck(List: list):
    length = len(List)
    for i in range(1, length//2):
        if List[i] != List[length-i]:
            return False
    return True


def ShiftRight(List: list):
        List.insert(0, List.pop())
        return List

def Str2L(s: str):
    tmp = list()
    for i in range(0, len(s)):
        tmp += s[i]
    return tmp


def L2Str(List: list):
    tmp = ''.join(List)
    return tmp


def RoundShifting(List: list, n: int):
    res = list()
    count = 0
    for i in List:
        num = Str2L(i)
        check = Str2L(i)
        count = 0
        while int(count) < int(n-1):
            num.append(num.pop(0))
            if num == check:
                break
            if L2Str(num) in List:
                List.remove(L2Str(num))
            count += 1
    return List

def Comb(n: int, k: int):
    tmp = list()
    List = list()
    List = '1'*k + '0'*(n-k)
    for i in itertools.permutations(List, n):
        num = ''.join(i)
        if num not in tmp:
            tmp.append(num)
    res = RoundShifting(tmp, int(n))
    return res


def Axis(num: list):
    List = len(num)
    if (List % 2) == 0:
        if SideCheck(num) == True:
            print(' -> ', L2Str(num[0:len(num)//2]), '  |  ', L2Str(num[len(num)//2:]));
            return True
        elif AncleCheck(num) == True:
            print( ' In axis number: ', num[0],'  -  ' , L2Str(num[1:List//2]), ';  In axis number:', num[List//2],'  -  ' , L2Str(num[List//2+1:List]))
            return True
    else:
        num = Str2L(num)
        temp = num.pop(0)
        if SideCheck(num) == True:
            num.insert(0, int(temp))
            print(' In axis number: ', num[0], '  -  ', L2Str(num[1:List]))
            return True
    return False


def FindSym(n: int, k: int):
    axis = 0
    count = 0
    List = list()
    List = Comb(n, k)
    for num in List:
        print('Number : ', num)
        axis = 0
        count = 0
        while int(count) < int(n):
            tmp = Axis(num)
            num = ShiftRight(Str2L(num))
            if tmp == True:
                axis += 1
            count += 1
        print('Axis count: ', axis, '\n')




#FindSym(length of number, count of "1" in number)
n = 8
k = 4
FindSym(n, k)
