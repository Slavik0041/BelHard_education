"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию в которой будет работать бесконечный цикл, увеличивая счетчик
на 1.
Нужно прервать цикл, когда счетчик станет равным 10 и вернуть значение счетчика

ПРИМЕРЫ
--------------------------------------------------------------------------------
lets_break() -> 10
"""


def lets_break() -> int:
    counter = 0
    while True:
        counter += 1
        break
    counter = 10
    return counter


if __name__ == '__main__':
    assert lets_break() == 10
    print('Решено!')
