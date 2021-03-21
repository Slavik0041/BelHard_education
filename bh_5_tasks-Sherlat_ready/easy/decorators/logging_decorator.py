"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""
user_name = 'Царь'


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        print(func(*args, **kwargs))
        print(f'Выполнено {func.__name__}')
    return wrapper


@log_decorator
def hello(name: str):
    result = f'Привет, {name}\n'
    return result


hello(user_name)
