from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    return HttpResponse('python starter     python essential    python advanced     python&Django')


def show_starter(request):
    return HttpResponse('1 - Введение в Python.  2 - Переменные и типы данных. 3 - Условные конструкции.'
                        '4 - Циклические конструкции.   5 - Функции. 6 - Списки.')


def show_essential(request):
    return HttpResponse('1 - Введение в ООП. 2 - Наследование и полиморфизм. 3 - Исключения. 4 - Итераторы и генераторы.'
                        '5 - Последовательности. 6 - Множества и отображения. 7 - Модули. 8 - Ввод и вывод.'
                        '9 - Элементы функционального программирования.')


def show_advanced(request):
    return HttpResponse('1 - Работа с сетью в Python: Socket и HTTP. 2 - Хранилища данных.'
                        '3 - Асинхронное и многопоточное программирование. 4 - Метаклассы. 5 - Библиотека Numpy.'
                        '6 - Типизированный Python. 7 - Модульное тестирование. 8 - Спецификация PEP 8.')

def show_django(request):
    return HttpResponse('1 - Введение в Django. 2 - Маршрутизация. 3 - Шаблоны и фильтры.')
