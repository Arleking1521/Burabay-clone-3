# Generated by Django 5.0.2 on 2024-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_people_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
    ]
