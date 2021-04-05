"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""
from math import pi
from abc import ABC


class Share(ABC):
    def get_perimeter(self):
        print(f'Посчитаем периметр фигуры: ')

    def get_square(self):
        print(f'Посчитаем площадь фигуры: ')


class Circle(Share):
    r: int

    def __init__(self, r=0):
        self.r = r

    def get_perimeter(self, r):
        dlina = 2 * pi * r
        print(f'Длина окружности с радиусом {r}: {dlina} ')

    def get_square(self, r):
        square = pi * r ** 2
        print(f'Площадь окружности с радиусом {r}: {square} \n')


class Rectangle(Share):
    a: int
    b: int

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def get_perimeter(self, a, b):
        perimetr = (a + b) * 2
        print(f'Периметр прямоугольника со сторонами '
              f'а = {a}, b = {b}: {perimetr} ')

    def get_square(self, a, b):
        perimetr = a * b
        print(f'Площадь прямоугольника со сторонами '
              f'а = {a}, b = {b}: {perimetr} \n')


class Square(Rectangle):
    def __init__(self, a=0):
        super().__init__(a)

    def get_perimeter(self, a):
        perimetr = 4 * a
        print(f'Периметр квадрата со стороной а = {a}: {perimetr} ')

    def get_square(self, a):
        perimetr = a ** 2
        print(f'Площадь квадрата со стороной а = {a}: {perimetr} \n')


circle = Circle()
Circle.get_perimeter(circle, 6)
Circle.get_square(circle, 6)

rectangle = Rectangle()
Rectangle.get_perimeter(rectangle, 3, 4)
Rectangle.get_square(rectangle, 3, 4)

square = Square()
Square.get_perimeter(square, 5)
Square.get_square(square, 5)
