# Generated by Django 4.2.4 on 2023-08-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]
