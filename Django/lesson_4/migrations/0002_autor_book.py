# Generated by Django 2.2.6 on 2019-10-27 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('date_born', models.DateField(verbose_name='Дата рождения')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year_of_publishing', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson_4.Autor')),
            ],
        ),
    ]