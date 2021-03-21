"""
Задача из собеседования в яндекс

Написать рекурсивную функцию generate_brackets, которая принимает длину -
количество пар скобок, и будет генерировать все возможные варианты
скобочных последовательностей


Например:
n = 3
((()))
(()())
(())()
()(())
()()()

n = 4
(((())))
((()()))
((())())
((()))()
(()(()))
(()()())
(()())()
(())(())
(())()()
()((()))
()(()())
()(())()
()()(())
()()()()
"""


def generator_brackets(n, sequence='', opened=0, closed=0):
    if len(sequence) != 2 * n:
        if opened < n:
            generator_brackets(n, sequence + '(', opened + 1, closed)
        if closed < opened:
            generator_brackets(n, sequence + ')', opened, closed + 1)
    else:
        print(sequence)


generator_brackets(3)