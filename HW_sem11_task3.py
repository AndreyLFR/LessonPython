class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(width=new_width, height=new_height)

    def __sub__(self, other):
        new_width = self.width - other.width if self.width - other.width else 0
        new_height = self.height - other.height if self.height - other.height else 0
        return Rectangle(width=new_width, height=new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}, где первое число - это ширина, а второе - высота.'

    def __repr__(self):
        return f'{self.width = }, {self.height = }'

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Периметр rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")