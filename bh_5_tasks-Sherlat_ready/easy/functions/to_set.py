"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(to_list: list) -> set:
    result = set(to_list)
    return result, len(result)


if __name__ == '__main__':
    assert to_set(['с', 'п', 'и', 'с', 'о', 'к']) == \
           ({'о', 'с', 'п', 'к', 'и'}, 5)
    print('Решено!')
