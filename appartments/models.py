from django.db import models


class Appartments(models.Model):
    title = models.CharField('Название аппартамента', max_length=255)
    city = models.CharField('Город', max_length=255)
    rooms = models.CharField('Комнат', max_length=255)
    place = models.CharField('Квадратных метров', max_length=255)
    floor = models.CharField('Этаж', max_length=255, null=True, blank=True)
    roomType = models.CharField('Тип (Дом или Квартира)', max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField('Описание')
    phone = models.CharField('Номер телефонма', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    image1 = models.ImageField(upload_to='appartments', null=True, blank=True)

    def __str__(self):
        return self.title