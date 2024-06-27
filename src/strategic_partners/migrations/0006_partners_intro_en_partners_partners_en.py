# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategic_partners', '0005_alter_partners_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='intro_en',
            field=models.TextField(null=True, verbose_name='Введение'),
        ),
        migrations.AddField(
            model_name='partners',
            name='partners_en',
            field=models.TextField(null=True, verbose_name='Список партнеров'),
        ),
    ]