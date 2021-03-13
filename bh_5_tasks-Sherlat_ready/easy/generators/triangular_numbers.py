"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 2
next(tn_gen) -> 6
next(tn_gen) -> 24

P.S Примерн навернео взят из другого задания.
По формуле не совпадает с ответами
"""


def triangular_numbers():
    for number in range(1, 10):
        Tn = (1 / 2) * number * (number + 1)
        yield Tn


tn_gen = triangular_numbers()

print(tn_gen)
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))


