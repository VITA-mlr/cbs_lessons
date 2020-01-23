from django.db import models

# Create your models here.


class Respond(models.Model):
    login = models.CharField(max_length=50, verbose_name='Ваше имя')
    respond = models.TextField(verbose_name="Ваш отзыв")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s: %s\n%s' % (self.login, self.respond, self.date)
