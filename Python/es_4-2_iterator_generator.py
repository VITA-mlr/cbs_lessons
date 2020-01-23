"""
task1:
Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

task2:
Перепишите решение первого задания с помощью генератора.
"""


class ListIterator:
    def __init__(self, collection):
        self.collection = collection
        self.cursor = len(self.collection)

    def __iter__(self):
        return ListIterator(self.collection)

    def __next__(self):
        self.cursor -= 1
        if self.cursor < 0:
            raise StopIteration()
        else:
            return self.collection[self.cursor]


def task1(some_list):
    """Ітератор списку"""

    my_iter = ListIterator(some_list)

    print(some_list)
    for el in my_iter:
        print('Елемент - ', el)


def task2(some_list):
    """Генератор списку"""

    index = len(some_list) - 1

    print(some_list)
    while index >= 0:
        yield some_list[index]
        index -= 1


def main():
    my_list = [1, 2, 3, 4, 5]

    print('ЗАВДАННЯ 1 - ІТЕРАТОР')
    task1(my_list)

    print('\nЗАВДАННЯ 2 - ГЕНЕРАТОР')
    for el in task2(my_list):
        print('Елемент - ', el)


if __name__ == "__main__":
    main()
