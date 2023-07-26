from django.db import models


class Product(models.Model):
    """
    Класс-модель товара
    """

    article = models.CharField(max_length=60, verbose_name='Артикул', unique=True)
    name = models.CharField(max_length=300, verbose_name='Наименование')
    price = models.CharField(verbose_name='Цена', max_length=25)

    def __str__(self):
        return self.name


class Counter(models.Model):
    """
    Класс-модель для подсчёта общего количества заявок
    """
    name = models.CharField(verbose_name='Заявки', max_length=10)
    num_of_entries = models.IntegerField(verbose_name='Количество заявок')

    def __str__(self):
        return f'Количество заявок - {self.num_of_entries}'
