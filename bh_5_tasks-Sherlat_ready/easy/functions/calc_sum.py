"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и  возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(*args):
    summa = 0
    for i in args:
        summa += i
    return summa
    # return sum(args)


if __name__ == '__main__':
    some_values = []
    while True:
        values = input('Введите число: ')
        if values == 'stop':
            break
        some_values.append(int(values))
    print(calc_sum(*some_values))
