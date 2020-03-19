from itertools import *

def check(num):
    l = len(num);
    for i in range(l//2):
        if num[i] != num[-1-i]:
            return 0;
    return 1;

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst
            
def listToString(s):  
    str1 = ""   
    for ele in s:  
        str1 += ele     
    return str1

def axisOfSymmetry(num):
    l = len(num);
    count = 0;
    if (l % 2 == 0):
        for i in range(l):
            #для 0 узлов
            if (check(num) == 1):
                #print(num);
                count+=1;
            #для двух узлов    
            #удалить два элемента проверить, потом добавить
            if (i < l//2):
                tmpf = list(num).pop(0);
                #print('pop0',num)
                tmpm = list(num).pop(l//2);
                #print('pop l//2',num, l)
                num = num[1:l//2]+ num[l//2+1:]
#print(num)
                if (check(num) == 1):
                    #print(num);
                    count+=1;
                #print('tmpf ', tmpf,' ', num[0:l//2-1] ,' ', tmpm ,' ', num[l//2-1:l])
                num = tmpf + num[0:l//2-1] + tmpm + num[l//2-1:l]
            num = shift(list(num), 1);
            num = listToString(num);
    else:
        for i in range(l):
            #запомним первый элемент и удалим его, потом добавим
            tmp = list(num).pop(0)
            num = num[1:];
            num = listToString(num);
            if (check(num) == 1):
                count+=1;
                #print(num);
            num = num+str(tmp);
    #print(count);
    return count

n = int(input());
k = int(input());
num = set()
str = "";
str +='1'*k;
str +='0'*(n-k);
#print(str)
for i in permutations(str, n):
    f=0;
    for j in range(n):
        if (listToString(shift(list(i), j)) in num):
            f=1;
    if f==0:    
        num.add(listToString(i))
for i in num:
    count = axisOfSymmetry(i);
    print(i,' ', count)
