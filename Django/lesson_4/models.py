from django.db import models

# Create your models here.


class ExamplesModel(models.Model):
    name = models.CharField(max_length=20)
    text = models.TextField()
    email = models.EmailField()
    #telefon_number = models.PositiveIntegerField()


class Autor(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    date_born = models.DateField(auto_now=False, verbose_name="Дата рождения")
    country = models.CharField(max_length=20, verbose_name="Страна")

    def __str__(self):
        #print("Имя - %s, фамилия - %s" %(self.first_name, self.last_name))
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    year_of_publishing = models.PositiveSmallIntegerField()
    text = models.TextField()

    def __str__(self):
        return self.title
