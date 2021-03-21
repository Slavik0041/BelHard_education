"""
Написать 2 генератора:
1) Генератор simple_number первый идет по всем простым числам
(число делится только на 1 и на само себя)
2) Генератор odd_simple, который используется значения первого и возвращает
из них нечетные
"""


def simple_number():
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


number = simple_number()
print(number)
print('Простые числа: ')
print(next(number))
print(next(number))
print(next(number))
print(next(number))

def odd_simple():
    for i in number:
        if i % 2 == 0:
            break
        else:
            yield i

simple = odd_simple()
print(simple)
print('Простые не четные числа: ')
print(next(simple))
print(next(simple))
print(next(simple))
print(next(simple))
print(next(simple))
print(next(simple))
print(next(simple))