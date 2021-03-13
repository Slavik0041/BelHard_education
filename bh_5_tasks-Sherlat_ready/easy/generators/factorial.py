"""
Написать генератор factorial, который возвращает подряд числа факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    a = 1
    for number in range(1, 10):
        a *= number
        yield a


factorial_gen = factorial()

print(factorial_gen)

print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
