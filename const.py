DB_COUNT_FIELDS = 5
DB_DELIMITER = '|'
DB_FILE_NAME = 'table_books.txt'
BOOK_STATUS = {
    0: 'выдана',
    1: 'в наличии',
}


APP_DESCRIPTION = """
Приложение для управления библиотекой книг.
Приложение предоставляет возможность работы с локальной базой данных
книг, на основе текстовго файла. База данных содержит информацию о книгах:
    - числовой идентификатор, уникальный для каждой книги
    - название книги
    - автор
    - год издания
    - статус ('в наличии' или 'выдана')

Доступные действия:
    - добавление информции о книге в базу данных
    - поиск книги по названию, автору или году выпуска
    - удаление книги
    - вывод списка всех книг
    - изменение статуса книги
"""

APP_HINTS = {
    'info': APP_DESCRIPTION,
    'help':
    """
Команды для управления приложением:
    add  - добавить новоую книгу
    del  - удалить книгу
    find - найти книгу по одному или нескольким ключам
    show - вывести список всех книг
    stat - установить статус книги 'в наличии' или 'выдана'
    info - справочная информация об этом приложении

    Подробная справка о команде: help <команда>, например: help del
    """,
    'exit': 'Команда для выхода из приложения.',
    'add':
    """
    Команда для добавления новой книги в базу данных. Формат команды:
    add <название книги>|<автор>|<год издания>
    """,
    'del':
    """
    Команда для удаления книги из базы данных. Нужно указать идентификатор.
    Формат команды:
    del <идентификатор>
    """,
    'find':
    """
    Команда для поиска книги в базе данных, нужно указать одну
    или несколько опций:
        -t <название>
        -a <автор>
        -y <год издания>
    Например:
        find -t чистый -y 2022
    будет искать книги со словом 'чистый' в названии и датой издания 2022 года.
    """,
    'show': 'Команда выводит список всех книг в базе данных',
    'stat':
    """
    Команда устанавливает указанный статус для книги с указанным
    идентификатором. Формат команды:
    stat <идентификатор> <код статуса>
        кодв статуса: 1 - в наличии, 0 - выдана
    Например:
        stat 256 1
    установит книге с идентификатором 256 статус 'в наличии'
    """,
}

ERR_NOT_SPECIFIED_AUTHOR = 'Автора книги нжно указать.'
ERR_NOT_SPECIFIED_TITLE = 'Название книги нужно указать.'
ERR_NOT_SPECIFIED_YEAR = 'Год издания книги должен быть указан.'
ERR_INVALID_YEAR = 'Год издания книги должен быть числом.'
ERR_INVALID_BOOK_DATA = 'Передана некорректная информация о книге.'
ERR_INVALID_BOOK_STATUS = 'Код статуса был неверно указан.'
ERR_INVALID_NUMERIC = 'Этот параметр должен быть числом.'
ERR_NOT_ENOUGHT_PARAMS = ('В команде передано недостаточное '
                          'количество параметров.')
