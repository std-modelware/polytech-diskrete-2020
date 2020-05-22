from itertools import permutations
import string
def dec_to_bin(x):
    return int(bin(x)[2:])

def count(bin):
    out = 0
    while(bin > 0):
        out += bin % 10
        bin = bin // 10
    return out
    
def Unique( l, one ):
    answer = []
    num = dec_to_bin(2**one - 1)
    num = num * 10**(l - one)
    #print(num)
    str1 = [int(x) for x in str(num)] 
    perm = permutations(str1)
    #for i in list(perm): 
    #print (i)
    for i in list(perm): 
        ii = list(i)
        #print (ii) 
        for j in range(0, l):
            tmp = ii.pop()
            ii.reverse()
            ii.append(tmp)
            ii.reverse()
            #print (ii, '*') 
            if(ii in answer):
                #print (ii, '***')
                answer.remove(ii)
        answer.append(list(i))
    return answer
           
           
def CheckPali(word):
    #print(word)
    return word == word[::-1] 

def Check2Side(curr):
    str1 = ''.join(str(e) for e in curr)
    #print(str1, '!!')
    return CheckPali(str1)
def CheckVertSide(curr):
    f1 = curr.copy()
    f1.pop(0)
    str1 = ''.join(str(e) for e in f1)
    #print(str1, '!!')
    return CheckPali(str1)

def Check2Vert(curr, l):
    f1 = curr.copy()
    #print(f1, '*0', l)
    f1.pop(int(l / 2))  
    f1.pop(0)
    #print(f1, '!vwrew')
    if l - 2 != 0:
        str1 = ''.join(str(e) for e in f1)
        #print(str1, '!!')
        return CheckPali(str1)
    return 0 

def Symm(l, word, fig):
    if l % 2 == 1: #ODD
        for j in range(0, l):
            tmp = fig.pop()
            #print(fig, "1")
            fig.reverse()
            #print(fig, "2")
            fig.append(tmp)
            #print(fig, "3")
            fig.reverse()
            print(fig, "^^")
            if CheckVertSide(fig):
                print('Symm is vert & side; side(mid)', word[int((l-1) / 2)], word[int((l-1) / 2) + 1 ],'vert:', word[0])
            
    else:          #EVEN
        for j in range(0, int(l/2)):
            tmp = fig.pop()   # do similar actions to Word (figure with named vertices) to visualise
            #print(fig, "1")
            fig.reverse()
            #print(fig, "2")
            fig.append(tmp)
            #print(fig, "3")
            fig.reverse()
            tmp1 = word.pop()
            #print(fig, "1")
            word.reverse()
            #print(fig, "2")
            word.append(tmp1)
            #print(fig, "3")
            word.reverse()
            #print(fig, "^^")
            if Check2Side(fig):
                print('Symm is 2 side; 1 side(mid)', word[l-1], word[0],'2 side(mid)', word[int(l/2)-1], word[int(l/2)])
            if Check2Vert(fig, l):
                print('Symm is 2 vert: ', word[0], word[int(l/2)])
            #print(fig, "(9)")



#Symm(4, [0, 1, 0, 1])
print('UPPERCASE is 1 vertices lowercase -- 0')
for i in range (3, 5):
    print('Length == ', i)
    for j in range (1, i):
        print(' №of 1 == ', j)
        classes = Unique(i, j)
        for k in classes:
            if len(k) == 1:
                k = [0 for m in range(1,i+1)]
            else:
                str1 = list()
                for m in range(0, len(k)):
                    if k[m] == 0:
                        str1.append(string.ascii_lowercase[m])
                    else:
                        str1.append(string.ascii_uppercase[m])
            print('    Figure is :', str1)
            Symm(i, str1, k)
                