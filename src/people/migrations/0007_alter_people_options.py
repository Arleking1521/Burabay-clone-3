# Generated by Django 5.0.2 on 2024-05-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_alter_people_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
    ]