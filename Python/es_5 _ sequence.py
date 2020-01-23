"""
task 1
Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной
в порядке возрастания.

task 2
Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
чисел и среднее арифметическое чисел из заданного диапазона.

task 3
Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
данного текста.
"""


def numeric(*args):
    some_str = str(*args)
    some_list = list(map(int, some_str.split()))

    some_list.sort()

    for el in some_list:
        print(el)


def my_function(*arg):
    my_list = [*arg]
    return my_list, sum(my_list)/len(my_list)


def text(*arg):
    str1 = str(*arg)
    list1 = str1.split()
    list1.sort()
    return list1


if __name__ == "__main__":
    print("\nЗавдання 1")
    print(numeric(input('Введіть числа для сортування ')))

    print('\nЗавдання 2')
    print(my_function(2, 5, 10, 3))
    print(my_function(9, 3))
    print(my_function(*range(6)))

    print("\nЗавдання 3")
    print(text(input('Введіть текст ')))
