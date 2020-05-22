from math import fabs
MAX_Length = 7
Max_Base = 11

def Decimal_Base(number, base):
    alphabet = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
    newNum = []
    while 1:
        dec, temp = divmod(number, base)
        if dec == 0:
            newNum[len(newNum):] = [alphabet[temp]]
            break
        number = dec
        newNum[len(newNum):] = [alphabet[temp]]
    newNum_=''.join(reversed(newNum))
    return newNum_


def Number_List(num, lenght, base):
    list_ = list()
    dec = int(num,base)
    for i in range(lenght):
        dec, temp = divmod(dec, base)
        list_[len(list_):] = [temp]
    return list_


def List_Number(num, base):
    total = 0
    temp = base ** (len(num) - 1)
    for i in range(len(num)):
        total = total+num[i] * temp
        temp = temp/base
    return total


def Find_Kaprekar_Number(length, base):
    total_list = []
    dimension = base ** length
    for dec_number in range(dimension):
        number = Decimal_Base(dec_number, base)
        list_ = Number_List(number, length, base)
        list_.sort()
        Min_len = List_Number(list_, base)
        list_.sort(reverse=True)
        Max_len = List_Number(list_, base)
        magic = Decimal_Base(int(Max_len - Min_len), base)
        if magic == number:
            total_list[len(total_list):] = [magic]
    return total_list


def Main():
    temp=list()
    #k=0
    for length in range(2, MAX_Length ):
        print('[Length: %d]\n'%(length))
        for base in range(2, Max_Base ):
            temp=Find_Kaprekar_Number(length, base)
            print('Base of number system -> %d:' % base)
            for k in range(len(temp)):
                   print( '%s\n' % (temp[k]))

Main()
