import os
import const
from book import Book


class BookList:
    """
    Клас для представления списка книг и связи его с файлом.
    Осуществляет поиск по списку, удаление элементов,
    изменение свойств элементов.
    """
    def __init__(self):
        self.__book_list = list()
        self.__current_free_id = 1
        if os.path.exists(const.DB_FILE_NAME):
            self.__read_from_file()
        else:
            with open(const.DB_FILE_NAME, 'w'):
                pass

    def __del__(self):
        self.__save_to_file()

    def __get_index(self, id) -> int:
        for idx, book in enumerate(self.__book_list):
            if book.id == id:
                return idx
        return -1

    def __read_from_file(self) -> None:
        with open(const.DB_FILE_NAME, 'r') as f:
            for line in f.readlines():
                self.__book_list.append(Book(*self._parse(line)))
                self.__current_free_id = max(
                    self.__current_free_id,
                    self.__book_list[-1].id + 1)

    def __save_to_file(self):

        with open(const.DB_FILE_NAME, 'w') as f:
            f.writelines('\n'.join(map(repr, self.__book_list)))

    def _parse(self, line: str) -> dict:
        """Разбор строки из файла """
        values = line.split(const.DB_DELIMITER)
        if len(values) < const.DB_COUNT_FIELDS:
            raise Exception(const.ERR_INVALID_BOOK_DATA)
        return values[:const.DB_COUNT_FIELDS]

    def add_book(self, title, author, year) -> bool:
        """Добавляет новую книгу в базу."""
        self.__book_list.append(
            Book(self.__current_free_id, title, author, year))
        self.__current_free_id += 1

    def show_books(self):
        """Выводит список всех книг."""
        for book in self.__book_list:
            print(book)

    def delete_book(self, id) -> bool:
        idx = self.__get_index(id)
        if idx < 0:
            return False
        else:
            self.__book_list.pop(idx)
            return True

    def find_books(self, **qwargs) -> list:
        found_books = []
        for book in self.__book_list:
            if book.compare(**qwargs):
                found_books.append(book)
        return found_books

    def change_status(self, id: int, status: int) -> bool:
        idx = self.__get_index(id)
        if idx < 0:
            return False
        else:
            self.__book_list[idx].status = status
            return True
