import time


class MySTR(str):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

class Archive:
    num_list = []
    str_list = []

    def __new__(cls, num, str_):
        instance = super().__new__(cls)
        instance.num = num
        instance.str_ = str
        cls.num_list.append(num)
        cls.str_list.append(str_)
        return instance

    def __str__(self):
        return f'Hi {self.num} {self.str_}'

    def __repr__(self):
        return f'{self.num} {self.str_}'

class Rectangle:
    def __new__(cls, a, b):
        instance = super().__new__(cls)
        instance.a = a
        instance.b = b
        return instance

    def square(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * (self.a + self.b)

    def __add__(self, other):
        return Rectangle(a=self.a + other.b, b=self.b + other.b)

    def __sub__(self, other):
        return Rectangle(a=self.a - other.b, b=self.b - other.b)

    def __eq__(self, other):
        return self.square() == other.square()

test = Rectangle(3, 4)
test2 = Rectangle(3, 4)

test3 = test + test2
print(test3.perimetr())

print(test2 == test)