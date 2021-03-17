"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


def fibonacci(num_count):
    fib_1, fib_2 = 0, 1
    if num_count < 1:
        print('Введите значение больше 1')
    else:
        for i in range(num_count):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            yield fib_2


gen_fib = fibonacci(5)
print(gen_fib)
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
