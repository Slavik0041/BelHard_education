"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""
from abc import ABC


class Animal(ABC):
    name: str
    a_type: str

    def __init__(self, name, a_type):
        self.name = name
        self.a_type = a_type

    def says(self):
        print(f'Животное по кличке {self.name} ')


class Cat(Animal):

    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        super().says()
        print(f'{self.a_type} кошка {self.name} говорит МЯУ \n')


class Dog(Animal):

    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        super().says()
        print(f'{self.a_type} пес {self.name} говорит ГАФ \n')


class Cow(Animal):
    def __init__(self, name, a_type):
        super().__init__(name, a_type)

    def says(self):
        super().says()
        print(f'{self.a_type} корова {self.name} говорит МУУ ')


cat = Cat('Анфиса', 'Домашняя')
dog = Dog('Барбос', 'Домашний')
cow = Cow('Мурка', 'Домашняя')
Cat.says(cat)
Dog.says(dog)
Cow.says(cow)