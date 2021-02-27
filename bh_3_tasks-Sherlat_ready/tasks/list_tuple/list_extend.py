"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая объединяет элементы 2х списков
"""
from copy import deepcopy


def list_extend(first_list: list, second_list: list) -> list:
    result = deepcopy(first_list)
    # TODO объединить result и second_list
    return result


if __name__ == '__main__':
    assert list_extend([1, 2], [3, 4]) == [1, 2, 3, 4]
    print('Решено!')
