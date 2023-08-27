from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    created_date = models.DateTimeField(verbose_name='дата создания')
    last_modified_date = models.DateTimeField(verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Feedback(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=25, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение')
