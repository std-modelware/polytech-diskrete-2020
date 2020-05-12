def kaprekar(number):
    list_of_digits = [int(d) for d in str(number)]
    list_of_digits1 = list_of_digits
    n = len(list_of_digits)
    if n < 4:
        tmp = 4 - n
        i = 0
        while i < tmp:
            list_of_digits.append(0)
            i = i+1
    list_of_digits.sort()
    min = int("".join(map(str, list_of_digits)))
    list_of_digits1.sort(reverse=True)
    max = int("".join(map(str, list_of_digits1)))
    print("%d -> min=%d, max=%d, -> %d" % (number, min, max, max - min))
    return max - min


magicNumber = [6174, 0]
usedNumber = []

from random import randint

number = randint(10, 100)

while True:
    number = kaprekar(number)
    if number in magicNumber:
        print("magic number")
        break
    if number in usedNumber:
        print("cycle")
        break
    usedNumber.append(number)
