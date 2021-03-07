"""
Написать функцию biggest_dict, которая принимает словарь (необязательный аргумент)
и неограниченное количество аргументов вида ключ-значение.

Если был передан словарь, то одна добавляет к нему все аргументы ключ-значение.
Если не был передан словарь, то создает новый из аргументов ключ-значение она составляет
словарь и возвращает словарь
"""


def beggest_dict(some_dict: dict = None, **kwargs):
    result = some_dict
    if result is None:
        result = {}

        result.update(kwargs)
        return result


if __name__ == '__main__':
    print(biggest_dict(name=123, noname=321))
    print(biggest_dict({'some': 1}, name=123, noname=321))
