"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая очистит множество
"""
from copy import deepcopy


def clear_set(collection: set) -> set:
    collection_copy = deepcopy(collection)
    # TODO вставить код сюда
    set.clear(collection_copy)
    return collection_copy


if __name__ == '__main__':
    assert clear_set({1, 2, 3}) == set()
    print('Решено!')
