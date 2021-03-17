"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    n = n / 2
    if n == 2:
        return True
    elif n > 2:
        return check_number(n)
    else:
        return False


print(check_number(89))
