"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернут количество элементов, которые равны некоторому
значению
"""
from typing import Any


def count_elements(collection: list, element: Any) -> int:
    # TODO вставить код сюда
    count = None
    return count


if __name__ == '__main__':
    assert count_elements([1, 2, 3, 2, 3], 2) == 2
    assert count_elements([1, 2, 3, 2, 3], 5) == 0
    print('Решено!')
