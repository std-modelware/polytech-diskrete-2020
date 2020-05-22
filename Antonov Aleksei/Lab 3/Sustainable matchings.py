# Men preference matrix.
# rows - women, columns - men
Men = [[3, 2, 4, 1],
       [2, 1, 3, 4],
       [2, 4, 1, 3],
       [3, 1, 4, 2]]

# Women preference matrix
# rows - men, columns - women
Women = [[4, 3, 1, 2],
         [3, 2, 4, 1],
         [1, 3, 4, 2],
         [3, 4, 2, 1]]
# Num of women/men
n = len(Men)

# List of women
# Brides[i] - number of man engaged to woman with number i
Brides = [-1] * n
# List of offers amount
# Offers_num - amount of offers, which man i has done
Offers_num = [0] * n
# List of men
# Grooms[i] - number of woman engaged to man with number i
Grooms = [-1] * n
# Rating of grooms
# Rating[i] - rating of groom engaged to woman with number i
Rating = [0] * n

# Number of pairs
k = 0


while k < n:

    print("{", end=' ')
    for i in range(n):
        if Grooms[i] != -1:
            print(f'{chr(ord("A") + i)}{chr(ord("a") + Grooms[i])}', end=' ')
    print("} -> ", end='')

    woman_number = -1
    man_number = 0
    for man_number in range(n):
        if Grooms[man_number] == -1:
            # Free man makes an offer to women with number Offers_num[man_number]
            woman_number = Men[man_number][Offers_num[man_number]] - 1
            Offers_num[man_number] += 1
            break
    if Brides[woman_number] == -1:
        k += 1
        Brides[woman_number] = man_number
        Grooms[man_number] = woman_number
        Rating[woman_number] = Women[woman_number][man_number]
        continue
    if Women[woman_number][man_number] > Rating[woman_number]:
        Grooms[Brides[woman_number]] = -1
        Grooms[man_number] = woman_number
        Rating[woman_number] = Women[woman_number][man_number]
        Brides[woman_number] = man_number

print("{", end=' ')
for i in range(n):
    if Grooms[i] != -1:
        print(f'{chr(ord("A") + i)}{chr(ord("a") + Grooms[i])}', end=' ')
print("}", end='')
