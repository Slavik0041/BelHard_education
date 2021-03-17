"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(lst):
    element = set()
    for i in lst:
        if i in element:
            print('Yes')
        else:
            element.add(i)
            print('No')


some_list = [1, 2, 3, 2, 6, 1, 7, 3]
print(yes_or_no(some_list))
