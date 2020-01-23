"""
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.
"""
from random import randint


with open("numbers.txt", 'w+') as file:
    numbers = [randint(0, 10) for i in range(10000)]
    for i in numbers:
        file.write(str(i))
