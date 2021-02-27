"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователи на сайте проходят тест

В программе определен шаблон для заполнения TEST_TEMPLATE.
Написать функцию copy_dict, которая вернет копию шаблона, чтобы пользователь
мог заполнять тест

ПРИМЕРЫ
--------------------------------------------------------------------------------
copy_dict(TEST_TEMPLATE) -> {
    'a1': None,
    'a2': None,
    'a3': None,
    'b1': None,
    'b2': None,
    'b3': None,
    'c1': None,
    'd1': None,
}
"""

TEST_TEMPLATE = {
    'a1': None,
    'a2': None,
    'a3': None,
    'b1': None,
    'b2': None,
    'b3': None,
    'c1': None,
    'd1': None,
}


def copy_dict(template: dict) -> dict:
    # TODO вставить код сюда
    template_copy = template
    return template_copy


if __name__ == '__main__':
    print('Подготовка вашего теста...')
    test = copy_dict(TEST_TEMPLATE)
    print('Можете приступать к выполнению!'
          if test == TEST_TEMPLATE and test is not TEST_TEMPLATE else
          'Ошибка. Попробуйте позже...')
