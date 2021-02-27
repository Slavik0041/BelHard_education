"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает длину списка
"""


def list_length(collection: list) -> int:
    # TODO написать код ниже
    result = len(collection)
    return result


if __name__ == '__main__':
    assert list_length([1, 2, 3, 4]) == 4
    print('Решено!')
