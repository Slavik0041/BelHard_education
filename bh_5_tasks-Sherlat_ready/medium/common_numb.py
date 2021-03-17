"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""
list_1 = [1, 4, 13, 18, 34, 8, 6]
list_2 = [8, 13, 7, 1, 35, 96, 7]


def common_numbers(list_one: list, list_two: list):
    some_list = []
    for i in list_one:
        for j in list_two:
            if i == j:
                some_list.append(i)
                break
    return sorted(some_list, reverse=True)


print(common_numbers(list_1, list_2))
