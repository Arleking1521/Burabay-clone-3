# Generated by Django 5.0.2 on 2024-05-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strategic_partners', '0004_alter_partners_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Партнер', 'verbose_name_plural': 'Партнеры'},
        ),
    ]
