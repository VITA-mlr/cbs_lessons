"""
Модифицируйте решение предыдущего задания

(Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.)

так, чтобы оно работало не с текстовыми, а бинарными файлами.
"""


from random import randint


with open("random_binery.bin", 'w+b') as file:
    number = [randint(0, 10) for i in range(10000)]
    print(len(number))
    for i in number:
        #print(int(i))
        file.write(bytes(i))