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

num = input();
l = len(num);
if (l % 2 == 0):
    for i in range(l):
        if (check(num) == 1):
            print(num);
        #print("before shi",num)
        num = shift(list(num), 1);
        num = listToString(num);
        #print("after shi",num)
else:
    for i in range(l):
        tmp = list(num).pop(0)
        #print("before pop",num, tmp)
        num = num[1:];
        num = listToString(num);
        #print("after pop", num)
        if (check(num) == 1):
            print(num);
        num = num+str(tmp);
        #num = listToString(num);
