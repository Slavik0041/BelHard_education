"""
Написать функцию calc_sum, которая принимает неограниченное количество целых
чисел и  возвращает их сумму

для расчета суммы можно воспользоваться функцией sum
"""


def calc_sum(*list_n):
    sum_num = 0
    for i in list_n:
        sum_num += i

    return sum(sum_num)