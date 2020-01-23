from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms, models


def show(request):
    return render(request, 'lesson_5/form.html')


def homework(request):
    #form = forms.HumanForm(request.POST)
    if request.method == 'POST':
        form = forms.HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lesson_5/homework/')
        else:
            return HttpResponse("Вы отправили пустую форму")
    return render(request, 'lesson_5/homework.html')


def show_html(request):
    return render(request, 'lesson_5/html_form.html')


def get_html_form(request):
    if request.method == 'GET':
        if 'get_input'in request.GET:
            return HttpResponse('Вас цікавить {}'.format(request.GET['get_input']))
        else:
            return HttpResponse("Вы отправили пустую форму")


def post_html_form(request):
    if request.method == 'POST':
        if 'post_input' in request.POST:
            return HttpResponse('Вас цікавить {}'.format(request.POST['post_input']))
        else:
            return HttpResponse("Вы отправили пустую форму")


def show_model(request):
    return render(request, 'lesson_5/model_form.html')


def show_class(request):
    return render(request, 'lesson_5/class_form.html')


def show_validator(request):
    return render(request, 'lesson_5/validator')
