"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На сервере хранятся данные пользователя. Пользователь решил очистить список своих
номеров.

Написать функцию clear_list, которая будет очищать переданный список.

ПРИМЕРЫ
--------------------------------------------------------------------------------
clear_list([1, 2, 3]) -> []
"""
from copy import deepcopy


user_data = {
    'first name': 'Ivan',
    'last name': 'Ivanov',
    'phones': [
        '+333221112266',
        '+333555879845'
    ]
}


def clear_list(collection: list) -> list:
    collection_copy = deepcopy(collection)
    # TODO вставить код сюда
    return collection_copy


if __name__ == '__main__':
    assert clear_list([1, 2, 3]) == []
    print('Решено!')
