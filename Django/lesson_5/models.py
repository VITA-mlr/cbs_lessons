from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=20, verbose_name="Фамилия")
    age = models.PositiveSmallIntegerField(verbose_name="Возрост")
    company = models.CharField(max_length=50, verbose_name="Компания")
    salary = models.PositiveSmallIntegerField(verbose_name="Зарплата")

    def __str__(self):
        return "Человек: {} {}({} лет)\nКомпания: {}\nЗарплата: {}".format(self.name,
                                                                           self.surname,
                                                                           self.age,
                                                                           self.company,
                                                                           self.salary)
