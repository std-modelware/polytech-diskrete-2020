import copy

def list_to_string(num):
    str = ""
    for i in range(0, len):
        str = str + numeric[num[i]]
    return str

def substruct(a, b):
    number = [None] * len
    for i in range(len - 1, -1, -1):
        s = a[i] - b[i]
        if s < 0 :
            s += base
            a[i-1] = a[i-1] - 1
        number[i] = s
    return number

def kaprekar(max):
    cycle = 0
    while True:
        print(list_to_string(max))#
        max.sort(reverse=True)
        cycle = cycle + 1
        min = max[::-1]
        number = substruct(max[:],min)
        str = list_to_string(number)
        if str in magicNumber:
            print('magic')
            break
        if max == sorted(number, reverse=True):
            magicNumber.append(str)
            cycle = cycle - 1
            print('magic')
            break
        if str in usedNumber:
            print('cycle')
            break
        usedNumber.append(str)
        max = number
    return cycle

def check(a, i):
    global cycle
    for j in range(a, -1, -1):
        max[i] = j
        if i + 1 == len:
            s = kaprekar(max)
            if s > cycle:
                cycle = s
        else:
            check(j, i+1)

numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

magicNumber = []
usedNumber = []
cycle = 0

file = open('table.csv', 'w')
file.write('"digits","base","loop","magic"\n')
for len in range(2, 5):
    for base in range(2, 10):
        cycle = 0
        max = [None] * len
        magicNumber.clear()
        usedNumber.clear()
        check(base - 1, 0)
        file.write('"%i","%i","%i", ' % (len, base, cycle))
        file.write('"[')
        buf = ""
        for k in magicNumber:
            buf = buf + k + ", "
        file.write(buf[:-2])
        file.write(']"\n')
file.close()