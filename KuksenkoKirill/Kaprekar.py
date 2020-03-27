def to10(number, base):
    return int(number, base)

def from10(number, base):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_number = []
    div = int(number)
    while div >= base:
        mod = alphabet[div % base]
        new_number.append(mod)
        div = div // base
    mod = alphabet[div % base]
    new_number.append(mod)
    new_number.reverse()
    return''.join(map(str, new_number))

def add(number, digits):
    return number.rjust(digits, '0')

def kaprekar(number, base):
    list_of_digits = [int(d, base) for d in str(number)]
    list_of_digits.sort()
    min = ''.join(map(str, list_of_digits))
    list_of_digits.sort(reverse=True)
    max = ''.join(map(str, list_of_digits))
    min10 = to10(min, base)
    max10 = to10(max, base)
    delta = max10 - min10
    return from10(delta, base)


def findmagical(digits, base):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    magical_numbers = []
    max = alphabet[base - 1] * digits
    max10 = to10(max, base)
    for i in range(0, max10):
        num = from10(i, base)
        number = kaprekar(add(num, digits), base)
        #print('%s - %s' % (add(number, digits), add(num, digits)))
        if add(number, digits) == add(num, digits):
            magical_numbers.append(number)
    return magical_numbers

def maxlength(digits, base):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    used = []
    magical = findmagical(digits, base)
    max = alphabet[base - 1] * digits
    max10 = to10(max, base)
    length = 0
    for i in range(0, max10):
        num = from10(i, base)
        number = num
        len = 0
        while True:
            used.append(number)
            number = kaprekar(add(number, digits), base)
            len = len + 1
            if number in magical:
                if len > length:
                    length = len
                break
            if number in used:
                len = len - 1
                if len > length:
                    length = len
                break
        used.clear()
    return length


maxdigits = 6
maxbase = 10

with open("result.csv", "w") as f:
    for digits in range(1, maxdigits + 1):
        for base in range(2, maxbase + 1):
            magical = findmagical(digits, base)
            length = maxlength(digits, base)
            f.write("number of digits - %s, base - %s\n" % (digits, base))
            print("magical numbers - %s" % magical, file=f)
            print("max length - %s" % length, file=f)
