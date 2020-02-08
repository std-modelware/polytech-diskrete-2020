#for m in range (k):,
#         i,q = divmod(i, r),
#         print(m,i,q),
#         d.append(q),
#     print(range(k)),

def kaprekar(number):
    list_of_digits = [int(d) for d in str(number)]
    list_of_digits.sort()
    min = int("".join(map(str, list_of_digits)))
    list_of_digits.sort(reverse=True)
    max = int("".join(map(str, list_of_digits)))
    print("%d -> min=%d, max=%d, -> %d" % (number, min, max, max - min))
    return max - min


magicNumber = [6174, 0]
usedNumber = []

number = 5654
while True:
    number = kaprekar(number)
    if number in magicNumber:
        print("magic number")
        break
    if number in usedNumber:
        print("cycle")
        break
    usedNumber.append(number)

