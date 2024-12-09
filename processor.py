import const
import service
from table import BookList


class Processor:
    def __init__(self):
        self.__book_list = BookList()
        print(const.APP_DESCRIPTION)
        print(const.APP_HINTS['help'])

    def __process_command(self, command_line) -> bool:
        """Обработка введенной команды."""
        params = command_line[1:]
        match command_line[0].lower():
            case 'add':
                self.__route_add(params)
            case 'del':
                self.__route_del(params)
            case 'find':
                self.__route_find(params)
            case 'show':
                self.__route_show(params)
            case 'stat':
                self.__route_status(params)
            case 'exit':
                return True
            case 'help':
                self.__route_hints(params)
            case 'info':
                self.__route_hints(['info'])
            case _:
                print('Введена неверная команда. '
                      'Для получения справки используйте команду help.')
        return False

    def process(self):
        """Циклический обрабочик ввода команд."""
        exit = False
        while not exit:
            line = input('#:')
            command = line.split() if len(line) > 0 else ['']
            try:
                exit = self.__process_command(command)
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue

    def __check_params(self, params: list, minimal_count_params: int) -> bool:
        if len(params) < minimal_count_params:
            raise Exception(const.ERR_NOT_ENOUGHT_PARAMS)

    def __check_numeric_param(self, param: str) -> int:
        if type(param) is str and not param.isnumeric():
            raise Exception(const.ERR_INVALID_NUMERIC)
        return int(param)

    def __route_hints(self, params: list):
        """Вывод справочной информации."""
        if len(params) > 0:
            command = const.APP_HINTS.get(params[0], None)
            if command:
                print(command)
        else:
            print(const.APP_HINTS['help'])

    def __route_add(self, params: list):
        """Обработка команды добавления новой книги в базу."""
        lines = ' '.join(params).split(const.DB_DELIMITER)
        self.__check_params(lines, 3)
        self.__book_list.add_book(*lines)

    def __route_del(self, params: list):
        """Обработка команды удаления книги."""
        self.__check_params(params, 1)
        id = self.__check_numeric_param(params[0])

        if self.__book_list.delete_book(id):
            print(f'Книга с ИД={params[0]} удалена из базы.')
        else:
            print(f'Не удалось удалить кигу с ИД={params[0]}.')

    def __route_find(self, params: list):
        self.__check_params(params, 2)
        books = self.__book_list.find_books(**service.parse_param(params))
        if len(books) == 0:
            print('По вашему запросу ничего не найдено.')
        else:
            print('По вашему запросу найдены книги:')
            for book in books:
                print(book)

    def __route_show(self, params: list):
        self.__book_list.show_books()

    def __route_status(self, params: list):
        """Обработка команды удаления книги."""
        self.__check_params(params, 2)
        id = self.__check_numeric_param(params[0])
        status = self.__check_numeric_param(params[1])

        if self.__book_list.change_status(id, status):
            print(f'Статус книги с ИД={id} изменен на '
                  f'"{const.BOOK_STATUS[status]}".')
        else:
            print(f'Книги с ИД={id} в базе не найдено.')
