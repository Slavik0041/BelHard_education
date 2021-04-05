"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:
    fio: str
    phone: str

    def __init__(self, fio, phone):
        self.fio = fio
        self.phone = phone


class LibraryReader(Person):
    id: int
    books: str

    def __init__(self, fio, phone, id, books):
        super().__init__(fio, phone)
        self.id = id
        self.books = books

    def take_book(self, *args):
        number_of_book = len(args)
        if number_of_book > 3:
            print(f'{self.fio} взял {number_of_book} книги! ')
        else:
            print(f'{self.fio} взял книги: {args}!!! ')

    def return_books(self, *args):
        number_of_book = len(args)
        if number_of_book > 3:
            print(f'{self.fio} вернул {number_of_book} книги! ')
        else:
            print(f'{self.fio} вернул книги: {args}!! ')


"""
Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы
  
Вот это не совсем понимаю как реализовать, написать еще одну функцию,
либо в return_books накрутить, но тогда в одной функции нагромаждено получается,
да и ошибок много наделать можно....

Я наверное что то упускаю, есть простое решение в 2 строчки, но я его не вижу (((( 
"""

person = Person('Петров В.В', '+375 44 937 99 92')
LibraryReader.take_book(person, 'Приключения', 'Словарь', 'Энциклопедия', 'Рассказы')
LibraryReader.return_books(person, 'Приключения', 'Словарь', 'Энциклопедия')
