"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет поверхностную копию списка

ПРИМЕРЫ
--------------------------------------------------------------------------------
"""


def copy_list(collection: list) -> list:
    # TODO вставить код сюда
    collection_copy = collection
    return collection_copy


if __name__ == '__main__':
    some_list = [1, 2, 3]
    col_copy = copy_list(some_list)
    assert col_copy is not some_list
    print('Решено!')
