# Generated by Django 5.0.2 on 2024-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoInfo', '0013_alter_ceodatas_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ceodatas',
            options={'verbose_name': 'Руководитель', 'verbose_name_plural': 'Информация о руководителе'},
        ),
    ]