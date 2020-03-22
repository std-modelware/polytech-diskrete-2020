import csv

f = open('C:/Users/shaoj/PycharmProjects/untitled/text.csv', 'w')

def PPRRIINNTT(num: list,size: int):
    for i in range(0,size,1):
        temp = num[i]
        f.write("%d" % temp)
    f.write(",")

def trans_to_10(num: list,n: int,size: int):
    sum = 0
    for i in range (0,size,1):
        sum = sum + num[size-i-1] * n**i
    return sum

def minuss(num1, num2, n, size):
    num3 = [0]*size
    for i in range(size-1,-1,-1):
        if(num1[i]-num2[i] < 0):
            num3[i] = num1[i] + n - num2[i]
            num1[i-1] = num1[i-1] - 1
        else:
            num3[i] = num1[i]- num2[i]
    return num3

def plus_add(num1,num2,n,size):
    num3 = [0]* size
    for i in range(size-1,-1,-1):
        if(num3[i] + num1[i] + num2[i] >= n):
            num3[i] = num3[i] + num1[i] + num2[i] - n
            num3[i-1] = 1
        else:
            num3[i] = num3[i] + num1[i] + num2[i]
    return num3

def s_o_s_f(num,n,size):
    num1 = [0]*size
    num2 = [0]*size

    for i in range(0,size,1):
        num1[i] = num[i]
        num2[i] = num[i]
    num1.sort(reverse = True)
    num2.sort(reverse = False)
    num3 = minuss(num1, num2, n, size)
    return num3


def Kaprekara(n, size):
    arr = [0]*size
    h = [0]*size
    h[size-1] = 1
    for i in range(1,n**size,1):
        arr = plus_add(arr,h,n,size)
        arr1 = s_o_s_f(arr,n,size)
        if(arr1 == arr):
            PPRRIINNTT(arr, size)


def Depth(n: int,size: int):
    arr = [0]*size
    h = [0]*size
    h[size-1] = 1
    temp = []
    k1 = 0
    k2 = 0
    for i in range(1, n ** size, 1):
        arr = plus_add(arr,h,n,size)
        num = trans_to_10(arr,n,size)
        temp.append(num)
        k1 = 1
        arr1 = s_o_s_f(arr,n,size)
        num1 = trans_to_10(arr1,n,size)
        while((num1 not in temp) and k1 < 1000 ):
            temp.append(num1)
            k1 = k1 + 1
            arr1 = s_o_s_f(arr1,n,size)
            num1 = trans_to_10(arr1, n, size)
        if(k1 > k2):
            k2 = k1
    return k2

def mmaaiinn_main():
    f.write('"Base";"Length";"Depth";"Kaprekara"\n')

    for n in range(2,11,1):
        for size in range(2,7,1):
            f.write('"%d";"%d";'%(n,size))
            f.write('"%d";' % (Depth(n,size)))
            Kaprekara(n,size)
            f.write('\n')

mmaaiinn_main()
