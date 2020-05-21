def Tob (base, num):
    newNum = ''

    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    #print(newNum)
    return newNum

def Kapr(num0, base):
    L  = [c for c in str(num0)]
    #print (L)
    L.sort()
    strings = [str(integer) for integer in L]
    a_string = "".join(strings)
    num1 = int(a_string, base)
    #print (L, num1)
    L.reverse()
    strings = [str(integer) for integer in L]
    a_string = "".join(strings)
    num2 = int(a_string, base)
    #print (L, num2)
    kap = num2 - num1
    kap2 = int(str(num0), base)
    #print (kap, kap2)
    if kap == kap2:
        #print (kap, kap2, L)
        return 1
    return 0


#Main
for i in range(2, 11):
    print("Pos = ", i)
    for j in range(2, 11):
        flag = 0
        print("  Len = ", j)
        num = i**(j - 1)
        while num < i**j:
            numi = Tob(i, num)
            #print(numi)
            if (Kapr(numi, i) == 1):
                flag = 1
                print("    Kapr:", numi)
            num += 1
        if flag == 0:
            print("  No Kapr :(")
