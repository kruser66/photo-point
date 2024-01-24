from django.db import models


class Exchange(models.Model):
    rate = models.DecimalField('Курс валюты', max_digits=15, decimal_places=6)
    currency = models.CharField('Код валюты', max_length=3)
    timestamp = models.DateTimeField('Время запроса', auto_now_add=True)

    class Meta:
        verbose_name = 'курс валюты'
        verbose_name_plural = 'Курсы валют'
