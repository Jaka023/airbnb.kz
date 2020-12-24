from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название слайда")
    price = models.CharField(max_length=255, verbose_name="Цена слайда")
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.title