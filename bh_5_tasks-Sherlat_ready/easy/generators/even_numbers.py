"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    for number in range(30):
        if number % 2 == 0:
            yield number


even_number = get_even_number()

'''
Что бы не писать принты, восползовался лайфхаком из занятия))) 
Мне показалось, такая запись более грамотная и в дальгейшем с ней можно,
что то делать или передать целым списком 
'''


def print_list_evan():
    list_even = []
    for i in get_even_number():
        list_even.append(i)
    print(list_even)


print_list_evan()
