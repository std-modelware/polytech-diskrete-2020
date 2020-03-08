# Классы

class MyClass:
    svar = 100 # переменная класса (статическая переменная)

    # конструктор
    def __init__(self, var):
        self.var = var

    def set_var(self, var):
        self.var = var

    def get_var(self):
        return self.var

    # договоренность
    def _private_method(self):
        return self.var + 1

print(dir(MyClass))

print(help(MyClass))

c1 = MyClass(10)
c2 = MyClass(20)

print(c1.var)
print(c2.var)

print(c1.svar)
print(c2.svar)

MyClass.svar = 200
print(c1.svar)
print(c2.svar)

c1.set_var(33)
print(c1.get_var())

print(MyClass.get_var(c1))

print(c1._private_method())

# Наследование
class MyClassBase:
    s1 = 99

    def __init__(self):
        self.v1 = 100

class MyClassDerived(MyClassBase):
    s2 = 999

    def __init__(self):
        super().__init__()
        self.v2 = 1000

c1 = MyClassBase()
c2 = MyClassDerived()

print(c1)
print(dir(c1))

print(c2)
print(dir(c2))