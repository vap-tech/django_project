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


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='ЧПУ')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='превью', **NULLABLE)
    created_date = models.DateTimeField(verbose_name='дата создания')
    is_public = models.BooleanField(default=True, verbose_name='опубликовано или нет')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')
