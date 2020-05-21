class Kaprekar():

    alf = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def conv(self, num):
        self.digit_list.clear()
        for i in range(0, self.dig, 1):
            self.digit_list.insert(0, self.alf[num % self.sys])
            num = num // self.sys

    def check_num(self):
        orig_dig_list = self.digit_list[:]
        orig_num = int("".join(self.digit_list), self.sys)
        self.digit_list.sort(reverse=True)
        max = int("".join(self.digit_list), self.sys)
        self.digit_list.sort()
        min = int("".join(self.digit_list), self.sys)
        num = max - min
        if num == orig_num:
            self.results.append("".join(orig_dig_list))

    def check_all(self, sys, dig):
        self.sys = sys
        self.dig = dig
        self.results = []
        self.digit_list = []
        num = list("0" + '0' * (self.dig - 1))
        self.digit_list = num[:]
        max = self.sys**self.dig
        for i in range(1, max + 1, 1):
            self.check_num()
            self.conv(int("".join(num), self.sys) + i)
        if self.results:
            print("Основание системы:", sys, "Кол-во цифр:", deg, '\n', self.results)
            self.results.clear()

k = Kaprekar()


for sys in range(2, 11, 1):
    for deg in range(2, 7, 1):
        k.check_all(sys, deg)
