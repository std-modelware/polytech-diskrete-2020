for n in range(2, 11):
    for w in range(1, 7):
        from array import *
        mas = array('i', []);
        print("range of system =", n, "number of elements =", w);
        for q in range(1, 1000):
            import random
            u = 0;

            while u == 0:
                if w == 1:
                    u = 1;
                a = random.randint(n ** (w - 1), n ** w - 1);
                v = a;
                num = "";

                while a != 0:
                    c = a % n;
                    a = a // n;
                    num = num + str(c);

                list_of_digits = [int(d, n) for d in str(num)]

                list_of_digits.sort(reverse = True);

                num = "";

                for i in range(len(list_of_digits)):
                    c = str(list_of_digits[i]);
                    num = num + c;

                v = int(num);
                c = v % n;
                v = v // n;
                while v != 0:
                    d = v % n;
                    v = v // n;
                    if d != c:
                        u = 1;
                    c = d;
                a = int(num, n);

            text = ''.join(reversed(num));

            b = int(text, n);

            from array import *
            data = array('i', [])

            c = 0;
            d = 0;

            while (a != 0) and (c != 1):
                a = a - b;
                if a != 0:
                    d = a;
                num = "";
                v = a;
                while v != 0:
                    c = v % n;
                    v = v // n;
                    num = num + str(c);

                list_of_digits = [int(d, n) for d in str(num)]

                list_of_digits.sort(reverse = True);

                num = "";

                for i in range(len(list_of_digits)):
                    c = str(list_of_digits[i]);
                    num = num + c;
                for i in range(0, w - len(list_of_digits)):
                    num = num + str('0');
                for i in range(len(data)):
                    if data[i] == a:
                        c = 1;
                if(c != 1):
                    data.insert(len(data), a)
                    if a != 0:
                        last = a;
                if a != 0:
                    a = int(num, n);

                    text = ''.join(reversed(num));

                    b = int(text, n);
                num = "";

            num = "";
            v = d;
            b = 0;
            while d != 0:
                c = d % n;
                d = d // n;
                if c != n - 1:
                    b = 1;
                num = num + str(c);
            text = ''.join(reversed(num));

            if (len(text) == 0) or (v != last) or ((b == 0) and (len(text) == n)):
                y = 0;
                for z in range(len(mas)):
                    if mas[z] == 0:
                        y = 1;
                if y == 0:
                    mas.insert(len(mas), 0);
            else:
                y = 0;
                for z in range(len(mas)):
                    if mas[z] == int(text):
                        y = 1;
                if y == 0:
                   mas.insert(len(mas), int(text));
            ar = array("i", []);
            data = d;
        for o in range(len(mas)):
            print(mas[o]);
        mas = [];