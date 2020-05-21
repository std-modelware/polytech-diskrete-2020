from itertools import *

data = [];

file = open('table.csv', 'w');
file.write('"N","M","Num equal","Num symmetry"\n');

def Check(num):
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            return 0;
    return 1;

def Symmetric(num):
    if len(num) % 2 == 0:
        count = 0;
        for i in range(len(num) // 2):
            if num[i] != num[-i - 1]:
                count = count + 1;
        if count < 1:
            return 1;
        else:
            c1 = num[0];
            c2 = num[len(num) // 2];
            w = len(num) // 2;
            del num[0];
            del num[len(num) // 2];
            count = 0;
            for i in range(len(num) // 2):
                if num[i] != num[-i - 1]:
                    count = count + 1;
            num.insert(0, c1);
            num.insert(w, c2)
            if count < 1:
                return 1;
            else:
                return 0;
    else:
        c = num[0];
        del num[0];
        count = 0;
        for i in range(len(num) // 2):
            if num[i] != num[-i - 1]:
                count = count + 1;
        num.insert(0, c);
        if count < 1:
            return 1;
        else:
            return 0;

def fakt(n):
    sum = 1;
    for r in range(1, n + 1):  
         sum = sum * r;
    return sum;

def bci(n, k):
    return fakt(n) // (fakt(k)*fakt(n-k));

def ar(num):
    bool = 0;
    p = 0;
    while bool != 1:
        for i in range(len(data)):
            if data[i] == num:
                bool = 1;
        if bool != 1:
            data.append(num.copy());
            if Symmetric(num) == 1:
                p = 1;
            for i in range(len(num) - 1):
                num[i], num[i + 1] = num[i + 1], num[i];
    return p;

def Count(num):
    bool = 0;
   # dat = [];
    count = 0;
    while bool != 1:
        for i in range(len(data)):
            if data[i] == num:
                bool = 1;
        if bool != 1:
            data.append(num.copy());
        if Symmetric(num) == 1:
            return 1;
        for i in range(len(num) - 1):
            num[i], num[i + 1] = num[i + 1], num[i];
    return 0;

def New(k, n):
    num = []
    for i in range(k):
        num.append(1);
    for i in range(k, n):
        num.append(0);
    st = bci(n, k);
    if len(data) == st:
        return num;
    bool = 0;
    while bool == 0:
        last = 0;
        bool = 1;
        for i in range(len(data)):
            if(num == data[i]):
                bool = 0;
                break;
        if bool == 0:
            last = len(num) - 1;
            while num[last] != 1:
                last = last - 1;
            if last == len(num) - 1:
                count = 1;
                del num[last];
                num.insert(last, 0);
                last = last - 1;
                while num[last] != 0 or num[last - 1] != 1:
                    if num[last] == 1:
                        del num[last];
                        num.insert(last, 0);
                        count = count + 1;
                    last = last - 1;
                del num[last - 1];
                num.insert(last - 1, 0);
                while count != -1:
                    del num[last];
                    num.insert(last, 1);
                    count = count - 1;
                    last = last + 1;
            else:
                del num[last];
                num.insert(last, 0);
                del num[last + 1];
                num.insert(last + 1, 1);
    return num;

for n in range(8, 16):
    for k in range(4, (n + 2) // 2):
        #print('N = ', n, 'K = ', k, '\n');
        data = [];
        num = [];
        for i in range(k):
            num.append(1);
        for i in range(k, n):
            num.append(0);
        st = bci(n, k);
        count = 0;
        q = 0;
        while len(data) < st:
            #for i in range(len(data)):
                #if data[i] == num:
                    #bool = 1;
            if bool != 1:
                #ar(num);
                #data = data + ar(num);
                count = count + 1;
                if ar(num) == 1:
                    q = q + 1;
            num = New(k, n);
        file.write('%i, %i, %i, %i \n' % (n, k, count, q));
        #print(count, q, '\n');