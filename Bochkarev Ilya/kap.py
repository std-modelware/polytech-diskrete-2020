class Kaprekar(object):

    def to_number(self, array):
        number = 0
        for i in range(self.radix):
            number += array[i] * (self.degree ** i)
        return number

    def column_subtraction(self, array1, array2):
        flag = False
        answer = []
        for i in range(self.radix):
            if flag:
                answer.append(array1[i] - array2[i] - 1)
            else:
                answer.append(array1[i] - array2[i])
            if answer[i] < 0:
                flag = True
                answer[i] += self.degree
            else:
                flag = False
        return answer

    def find_const_for_num(self):
        arr_of_const = []
        arr_of_all = []
        arr_of_all_in_sys = []
        copy = self.digit.copy()
        copy.sort()
        reverse = copy.copy()
        reverse.reverse()
        arr_of_all.append(self.to_number(self.digit))
        arr_of_all_in_sys.append(self.digit.copy())
        while True:
            new = self.column_subtraction(copy, reverse)
            new_number = self.to_number(new)
            if arr_of_all.count(new_number) != 0:
                index = arr_of_all.index(new_number)
                for i in range(len(arr_of_all_in_sys) - index):
                    arr_of_const.append(arr_of_all_in_sys[i + index])
                return arr_of_const
            else:
                arr_of_all.append(new_number)
                arr_of_all_in_sys.append(new)
            copy = new.copy()
            copy.sort()
            reverse = copy.copy()
            reverse.reverse()

    def __init__(self, radix, degree):
        self.radix = radix
        self.degree = degree
        self.digit = []
        all_const = []
        for i in range(radix):
            self.digit.append(0)
        all_const.append(self.find_const_for_num())
        for i in range(degree ** radix - 1):
            self.digit[0] += 1
            for j in range(radix):
                if self.digit[j] == degree:
                    self.digit[j] = 0
                    self.digit[j + 1] += 1
            temp = self.find_const_for_num()
            for j in range(len(temp)):
                temp[j].reverse()
            flag = True
            for j in range(len(all_const)):
                flag = True
                for t in range(len(all_const[j])):
                    flag = True
                    for y in range(radix):
                        if all_const[j][t][y] != temp[0][y]:
                            flag = False
                    if flag:
                        break
                if flag:
                    break
            if not flag:
                all_const.append(temp)
        f.write("System base - " + str(degree) + " Number of digits - " + str(radix) + "\n")
        for i in range(len(all_const)):
            f.write(str(all_const[i]) + "\n")


f = open('answer.txt', 'w')
for k in range(2, 4):
    for p in range(2, 4):
        m = Kaprekar(p, k)
f.close()
