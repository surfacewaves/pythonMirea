"""
Этот модуль содержит классы и функции для работы с MyDict
"""


class MyDict:
    """
    Класс словаря MyDict - аналога встроенного в Python словаря dict.
    """

    def __init__(self):
        """
        Конструктор класса MyDict
        """
        self.data = []

    def __getitem__(self, key):
        """
        Метод получения значения по ключу (перегрузка [])
        :param key:
        :return:
        """
        for k, v in self.data:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        """
        Перегрузка []
        :param key:
        :param value:
        :return:
        """
        for i, (k, v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)
                return
        self.data.append((key, value))

    def __delitem__(self, key):
        """
        Перегрузка del
        :param key:
        :return:
        """
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]
                return
        raise KeyError(key)

    def __len__(self):
        """
        Перегрузка len
        :return:
        """
        return len(self.data)

    def __repr__(self):
        """
        Перегрузка repr
        :return:
        """
        return repr(self.data)

    def __iter__(self):
        """
        Перегрузка iter
        :return:
        """
        return iter(self.data)

    def clear(self):
        """
        Очистка словаря
        :return:
        """
        self.data = []

    def copy(self):
        """
        Копирование словаря
        :return:
        """
        return self.data

    def values(self):
        """
        Получение списка значений
        :return:
        """
        return [v for k, v in self.data]

    def pop(self, key):
        """
        Удаление элемента по ключу
        :param key:
        :return:
        """
        self.__delitem__(key)


class TestClass:
    def WOW(self):
        pass


def main():
    d = MyDict()
    d['a'] = 35
    print("len = ", len(d))
    print("d[a] = ", d['a'])
    d['123'] = 3
    assert d['a'] == 35
    assert d['123'] == 3
    print(d)
    print()

    print("циклы:")
    for k, v in d:
        print(k, v)
    print()

    print("вложенный цикл")
    for k in d:
        for v in k:
            print(v)
    print()

    d.clear()
    print(d)
    print()

    d['a'] = 35
    d.pop('a')
    print(d)


if __name__ == '__main__':
    main()
