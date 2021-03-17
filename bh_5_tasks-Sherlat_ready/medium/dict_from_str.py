"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(str_str: str):
    my_dict = {}
    for key in str_str:
        if my_dict.get(key):
            my_dict[key] += 1
        else:
            my_dict[key] = 1
    return my_dict


print(dict_from_str(STR_VAL))
