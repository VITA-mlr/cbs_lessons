"""
Взяв за основу код примера 06-iterable_with_an_iterator.py, расширьте функциональность класса MyList,
добавив методы для очистки списка, добавления элемента в произвольное место списка, удаления
элемента из конца и произвольного места списка.
"""


class MyList(object):
    """Класс списка"""

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам
        # последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


    ##########################################################################################################
    """ Домашні завдання:
        методи clear(), del_el(), add_el()"""

    def clear(self):
        self._head = None
        self._tail = None
        self._length = None

    def del_el(self, index):
        if index >= 0:
            if not 0 <= index < len(self):
                raise IndexError('list index out of range')
            node = self._head
            for _ in range(index):
                node = node.next

        else:
            if not 0 <= abs(index) < len(self):
                raise IndexError('list index out of range')
            node = self._tail
            for _ in range(1, abs(index)):
                node = node.prev

        if node.prev is None:
            self._head = node.next
            node.next.prev = None

        elif node.next is None:
            self._tail = node.prev
            node.prev.next = None

        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self._length -= 1

    def add_el(self, index, element):
        node = MyList._ListNode(element)

        if index >= len(self):
            raise AttributeError("Список меншого розміру ")

        if index == 0:
            node.next = self._head
            self._head.prev = node
            self._head = node

        else:
            next_node = self._head
            for i in range(index):
                next_node = next_node.next

            next_node.prev.next = node
            next_node.prev.prev = node
            node.prev = next_node.prev
            node.next = next_node

        self._length += 1


def main():
    # Створюємо список
    my_list = MyList([1, 2, 5, 4, 6])

    print('\n', my_list)
    print(' ')

    # Видаляємо і-тий елемент з списку
    my_list.del_el(2)
    print(f'Видаляємо 2-ий елемент: {my_list}')
    print(" ")

    # Видаляємо і-тий елемент з списку
    my_list.del_el(-3)
    print(f"Cписок з видаленим елементом -3: {my_list}")
    print(' ')

    # Додаємо елемент на початок список
    my_list.add_el(0, 7)
    my_list.add_el(0, 99)
    print(f'Додаємо елемент на початок списку: {my_list}')
    print(' ')

    #Додаємо елемент по заданому індексу
    my_list.add_el(4, 12)
    print(f'Додаємо елемент 12 по заданому індексу 4: {my_list}')
    print(' ')

    # Очистка списку
    my_list.clear()
    print(f'Очистили список : {my_list}')


if __name__ == '__main__':
    main()
