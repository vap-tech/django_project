# Generated by Django 4.2.4 on 2023-09-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_current_version',
            field=models.BooleanField(verbose_name='Актуальная версия'),
        ),
    ]
