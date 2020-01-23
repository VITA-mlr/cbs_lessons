"""
task1
Даны две строки. Выведите на экран символы, которые есть в обоих строках.

task2
Создайте словарь с ключами-строками и значениями-числами. Создайте функцию, которая принимает
произвольное количество именованных параметров. Вызовите её с созданным словарём и явно
указывая параметры
"""


def task1():
    map1 = frozenset('Hello, world!')
    map2 = set('Hello, Vasya!')

    map3 = map1.intersection(map2)      # Возвращает пересечение — элементы данного множества, также присутствующие в
                                        # указанных объектах.  -> set/frozenset.

    map4 = map2 & map1      # можно использовать оператор амперсанд — &.
    print(map3)
    print(map4)
    for i in map4:
        print(i)


def task2():
    mydict = {'one': 1,
              'two': 2,
              'three': 3,
              }

    def myfunc(*kwargs):
        print(*kwargs)

    myfunc(mydict['two'])


if __name__ == '__main__':
    task1()
    task2()
