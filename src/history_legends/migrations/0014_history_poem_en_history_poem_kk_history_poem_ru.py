# Generated by Django 5.0.2 on 2024-06-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_legends', '0013_rename_info_kz_history_info_kk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='poem_en',
            field=models.TextField(null=True, verbose_name='Стихотворение'),
        ),
        migrations.AddField(
            model_name='history',
            name='poem_kk',
            field=models.TextField(null=True, verbose_name='Стихотворение'),
        ),
        migrations.AddField(
            model_name='history',
            name='poem_ru',
            field=models.TextField(null=True, verbose_name='Стихотворение'),
        ),
    ]
