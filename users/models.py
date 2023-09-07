from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class Country(models.Model):
    country = models.CharField(max_length=40, verbose_name='страна')
    description = models.TextField(max_length=200, verbose_name='описание')
    flag = models.ImageField(upload_to='users/country/', verbose_name='превью', **NULLABLE)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

