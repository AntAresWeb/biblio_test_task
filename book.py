import const


class Book:
    """Класс для представления объекта книги"""
    def __init__(self, id, title, author, year, status=1):
        data = self.clean_data(locals())
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.year = data['year']
        self.status = data['status']

    def clean_data(self, data: dict) -> dict:
        if len(data['title']) == 0:
            raise Exception(const.ERR_NOT_SPECIFIED_TITLE)

        if len(data['author']) == 0:
            raise Exception(const.ERR_NOT_SPECIFIED_AUTHOR)

        try:
            data['status'] = int(data['status'])
        except ValueError:
            raise Exception({'Статус': const.ERR_INVALID_YEAR})
        if data['status'] not in [0, 1]:
            raise Exception(const.ERR_INVALID_BOOK_STATUS)

        try:
            data['id'] = int(data['id'])
        except ValueError:
            raise Exception({'ИД': const.ERR_INVALID_NUMERIC})

        try:
            data['year'] = int(data['year'])
        except ValueError:
            raise Exception({'Год издания': const.ERR_INVALID_YEAR})

        return data

    def __str__(self) -> str:
        data = {
            'ИД': self.id,
            'Название': self.title,
            'Автор': self.author,
            'Год издания': self.year,
            'Статус': const.BOOK_STATUS.get(self.status, 'не известен')
        }
        return str(data)

    def __repr__(self):
        values = map(str, vars(self).values())
        return const.DB_DELIMITER.join(values)

    def compare(self, **qwargs) -> bool:
        for key, critery_list in qwargs.items():
            try:
                value = getattr(self, key)
            except AttributeError:
                continue
            if type(value) is str:
                value = value.lower()
                if not all(critery in value for critery in critery_list):
                    return False
            else:
                if not all(int(critery) == value for critery in critery_list):
                    return False
        return True
