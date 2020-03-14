def numerics(n, maxLen):
 #разделение на цифры # Яворук Т.О.   
    b = []
    n = int(n)
    while n > 0:
        b.append(str(n % 10))
        n = n // 10;
    while (len(b)< maxLen):
        b.append('0');
    return b;

def kaprekar_step(L, base = 10):
   #разность двух чисел # Яворук Т.О. 
    n1 = (''.join(str(x) for x in sorted(L)));
    n2 = (''.join(str(x) for x in sorted(L,reverse=True)))
    n10 = convert(n1, 10, base);
    n20 = convert(n2, 10, base);
    return str(abs(int(n10)-int(n20)));      

def convert(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, int(from_base))
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]

def kaprekar_loop(n,base = 10):
   # шагb капрекара # Яворук Т.О. 
    n_old = str(n);
    nums = list();
    while((nums.count(n) == 0)):
        nums.append(n);
        nk = kaprekar_step(numerics(n,len(n_old)), base);
        n = convert(str(nk), base, 10);
    if (nums.count(n) != 0) and (nums[-1] != n):
        nums.append(n);
    return nums

#631764

i=1
n= 2;
s = {}
l1 =len(convert(1,2,10));
m_last = 2;
for m in 2,3,4,5,6,7,8,9,10:
    i = 1;
    
    while len((convert(i,m,10))) < 7:
        i_con=convert(i,m,10)
        if (l1 != len(i_con)):
            print(l1,' ',m_last,' ',s);
            l1 = len(i_con);
            n = n + 1;
            m_last = m;
            s.clear();
        n = 2;
        nums = kaprekar_loop(i_con,m);
        #print (nums)
        if (nums.count(nums[-1]) == 1): #это не цикл
            while (len(nums[-1]) < len(i_con)):
                nums[-1] = '0'+nums[-1];
            if (s.get(nums[-1]) == None):
                s[nums[-1]] = len(nums)-1;
            else:
                s[nums[-1]] = max(len(nums)-1, s[nums[-1]])
        nums.clear();
        i = i+1;
print(l1,' ',m_last,' ',s);
