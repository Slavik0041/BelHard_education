"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(s_dict):
    result = 1
    for i in s_dict.values():
        print(i)
        result *= i
    return result


print(multiply_dict_values(SOME_DICT))
