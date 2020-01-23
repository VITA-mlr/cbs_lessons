"""
Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.
"""


my_list = [x for x in range(20)]
print(my_list)

square_list1 = [x**2 for x in my_list if x % 2 != 0]
print('\nЗа допомого генераторів-виразів: ', square_list1)

square_list2 = list(map(lambda x: x**2, list(filter(lambda x: x % 2 != 0, my_list))))
print('\nЗа допомогою функцій вищого порядку: ', square_list2)
