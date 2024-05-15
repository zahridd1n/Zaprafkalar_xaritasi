from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''Zaprafkalarni turlari  yani Metan,Prapan,'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Zaprafka(models.Model):
    """Zaprafka  haqida malumotlar"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    lat = models.CharField(max_length=255, blank=True)
    lan = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='zaprafka/', blank=True, null=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name

    @property
    def categorys(self):
        return ZaprafkaCategory.objects.filter(zaprafka=self)


class ZaprafkaCategory(models.Model):
    """Zaprafka  haqida malumotlar"""
    zaprafka = models.ForeignKey(Zaprafka, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name}| ({self.zaprafka.name})"
