"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multyply(n):
    def closure(x):
        return n * x

    return closure()


'''
Тут не совсем понимаю как првоерку написать
Попробовал по разному, но что то упускаю

if __name__ == '__main__':
    assert closure(5) == 10
    print('Решено!')
'''
