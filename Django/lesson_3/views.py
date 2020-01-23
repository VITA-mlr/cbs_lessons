from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . import forms, models
# Create your views here.


def show(request):
    levels = ['python starter', 'python essential', 'python advanced', 'python Django']
    content = {
        'text': 'Выберите интерисующий Вас курс.',
        'levels': levels,
        'python_starter': ['Введение в Python', 'Переменные и типы данных', 'Условные конструкции',
                           'Циклические конструкции', 'Функции', 'Списки'],
        'python_essential': ['Введение в ООП', 'Наследование и полиморфизм', 'Исключения', 'Итераторы и генераторы',
                             'Последовательности', 'Множества и отображения', 'Модули', 'Ввод и вывод',
                             'Элементы функционального программирования'],
        'python_advanced': ['Работа с сетью в Python: Socket и HTTP', 'Хранилища данных',
                            'Асинхронное и многопоточное программирование', 'Метаклассы', 'Библиотека Numpy',
                            'Типизированный Python', 'Модульное тестирование', 'Спецификация PEP 8'],
        'python_Django': ['Введение в Django', 'Маршрутизация', 'Шаблоны и фильтры', 'Модели'],
    }
    return render(request, 'lesson_3/cbs.html', content)


def show_starter(request):
    content = {
        'text': 'python starter',
        'levels': ['python starter', 'python essential', 'python advanced', 'python Django'],
        'python_starter': ['Введение в Python', 'Переменные и типы данных', 'Условные конструкции',
                           'Циклические конструкции', 'Функции', 'Списки'],
    }
    return render(request, 'lesson_3/starter.html', content)


class RespondFormView(TemplateView):
    form_contact = forms.RespondForm

    def post(self, request):
        form = forms.RespondForm(request.POST)
        context = {
            'form': form,
            'levels': ['python starter', 'python essential', 'python advanced', 'python Django'],
        }
        if form.is_valid():
            form.save()
            return redirect('/lesson_3/respond/')
        else:
            return render(request, 'lesson_3/respond.html', context)

    def get(self, request):
        context = {
            'form': self.form_contact,
            'data': models.Respond.objects.all(),
            'levels': ['python starter', 'python essential', 'python advanced', 'python Django'],
        }

        return render(request, 'lesson_3/respond.html', context)

"""
def file_input_respond(request):
    name = request.GET['name']
    respond = request.GET['text']
    date = request.GET['date']

    with open('somefile.text', 'w') as file:
        file.write('Имя: ' + name + '\n')
        file.write('Отзыв: ' + respond + '\n')
        file.write('Создан: ' + date)
"""