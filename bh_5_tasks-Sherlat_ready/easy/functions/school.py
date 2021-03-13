"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(data: dict) -> dict:
    for k, v in data.items():
        data[k] = v + 1
    return f'Увеличил кол-во учеников на +1: {data}'


def decr_students(data: dict) -> dict:
    for k, v in data.items():
        if v > 0:
            data[k] = v - 1
    return f'Уменьшил кол-во учеников на -1: {data}'


'''
Тут у меня есть пару вопросов

- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
Я понял что мне нужно передать название класса, в данном случае  incr_students,
но я не сосвсем понимаю, как мне с этим работать((( 

И мне кажется, что если все же нужно передать incr_students, 
то он не правильно реализован, он заточен на +1 для значение словаря, 
как перевернуть, что бы он добавлял +1 ключ словаря, не меняя исходную функцию 
'''


def add_class(data: dict) -> dict:
    plus_class = {'9a': 0}
    data.update(plus_class)
    return f'Добавил класс в школу: {data}'


def remove_class(data: dict) -> dict:
    data.popitem()
    return f'Отчислил класс за поведение)))): {data}'


def calc_students(data: dict) -> dict:
    return f'Учеников в школе: {sum(set(data.values()))}'


print(incr_students(school_data))
print(decr_students(school_data))
print(add_class(school_data))
print(remove_class(school_data))
print(calc_students(school_data))
