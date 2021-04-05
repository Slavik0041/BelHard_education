"""
Описать класс Transport, у которого следующие атрибуты:

- brand - фирма, выпустившая транспорт
- model - модель
- issue_year - год выпуска
- color - цвет

Определить методы:

- move - который делает raise NotImplementedError

Описать класс Car, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- engine_type

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} проехала {km} километров"

Описать класс Airplane, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- lifting_capacity - грузоподъемность

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} пролетел {km} километров"
"""


class Transport:
    brand: str
    model: str
    issue_year: int
    color: str

    def __init__(self, brand, model, issue_year, color):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    def move(self):
        raise NotImplementedError


class Car(Transport):
    mileage: int
    engine_type: str

    def __init__(self, brand, model, issue_year, color, engine_type, mileage):
        super().__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.engine_type = engine_type

    def move(self, km):
        self.mileage += km
        print(f'{self.brand} {self.model} проехала {self.mileage} километров')


audi = Car('Audi', 'A6', 2005, 'Silver', 'Бензин', 245000)
Car.move(audi, 1200)


class Airplane(Transport):
    lifting_capacity: str
    mileage: int

    def __init__(self, brand, model, issue_year, color, lifting_capacity, mileage):
        super().__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.engine_type = lifting_capacity

    def move(self, km):
        self.mileage += km
        print(f'{self.brand} {self.model} пролетел {self.mileage} километров')


samolet = Airplane('Bristell', 'NG-6', 2015, 'Silver', 'Топливо', 87500)
Airplane.move(samolet, 300)
