"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""

number_list = []

def list_number(n):
    if n == 0:
        return number_list
    ostatok = n % 10
    number_list.append(ostatok)
    list_number(n // 10)


list_number(56909)
print(f'Список цифр числа:{number_list}')


def sum_number(sum_list):
    sum_number_list = 0
    for i in sum_list:
        sum_number_list += i
    return sum_number_list


print(f'Сума цифр числа: {sum_number(number_list)}')

'''
Пробовал в одну функцию все запихнуть,
раз я могу number_list.append(ostatok),
то почему я не моуг sum_number_list += ostatok 

Но у меня ничего не получилось, либо бред какой-то, либо вообще не работает
Почти 2 часа над этим эксперементом просидел)))) 
'''
