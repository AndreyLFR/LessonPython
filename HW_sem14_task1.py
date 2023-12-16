class NegativeValueError(Exception):

    def __init__(self, *args):
        self.message = args if len(args) != 0 else None

    def __str__(self):
        return f'NegativeValueError Ширина должна быть положительной, а не {self.message}'


class Rectangle:
    """
    >>> r1 = Rectangle(5)
    >>> r1.width
    5
    >>> r4 = Rectangle(-2)
    f'HW_sem14_task1.NegativeValueError: NegativeValueError Ширина должна быть положительной, а не (-2,)'
    """

    def __init__(self, width, height=None):
        if height is None:
            height = width
        if not isinstance(width, int) or width < 0:
            raise NegativeValueError(width)
        if not isinstance(height, int) or height < 0:
            raise NegativeValueError(height)
        self.width = width
        self.height = height


    def perimeter(self):
        """
                Вычисляет периметр прямоугольника.
                Возвращает:
                - int: периметр прямоугольника
                """
        return 2 * (self.width + self.height)

    def area(self):
        """
                Вычисляет площадь прямоугольника.
                Возвращает:
                - int: площадь прямоугольника
                """
        return self.width * self.height

    def __add__(self, other):
        """
                Определяет операцию сложения двух прямоугольников.
                Аргументы:
                - other (Rectangle): второй прямоугольник
                Возвращает:
                - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
                """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
                Определяет операцию вычитания одного прямоугольника из другого.
                Аргументы:
                - other (Rectangle): вычитаемый прямоугольник
                Возвращает:
                - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
                """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
                Определяет операцию "меньше" для двух прямоугольников.
                Аргументы:
                - other (Rectangle): второй прямоугольник
                Возвращает:
                - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
                """
        return self.area() < other.area()

    def __eq__(self, other):
        """
                Определяет операцию "равно" для двух прямоугольников.
                Аргументы:
                - other (Rectangle): второй прямоугольник
                Возвращает:
                - bool: True, если площади равны, иначе False
                """
        return self.area() == other.area()

    def __le__(self, other):
        """
                Определяет операцию "меньше или равно" для двух прямоугольников.
                Аргументы:
                - other (Rectangle): второй прямоугольник
                Возвращает:
                - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
                """
        return self.area() <= other.area()

    def __str__(self):
        """
                Возвращает строковое представление прямоугольника.
                Возвращает:
                - str: строковое представление прямоугольника
                """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
                Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.
                Возвращает:
                - str: строковое представление прямоугольника
                """
        return f"Rectangle({self.width}, {self.height})"


rect1 = Rectangle(5, 9)
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

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)