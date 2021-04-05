"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n
- метод generate, который принимает длину последовательности n
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    sequence: list

    def __init__(self, n: int):
        self.generate(n)

    def generate(self, n):
        self.sequence = [random.randint(-10, 10) for i in range(n)]
        return self.sequence

    def print_seq(self):
        print(self.sequence)


rs = RandSequence(4)
rs.print_seq()
rs.generate(8)
rs.print_seq()
