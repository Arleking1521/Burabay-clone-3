# Generated by Django 5.0.2 on 2024-06-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0003_remove_science_addinfo_kk_remove_science_addinfo_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='title',
            field=models.TextField(verbose_name='Основыне пункты достижений'),
        ),
        migrations.AlterField(
            model_name='science',
            name='title_kk',
            field=models.TextField(null=True, verbose_name='Основыне пункты достижений'),
        ),
        migrations.AlterField(
            model_name='science',
            name='title_ru',
            field=models.TextField(null=True, verbose_name='Основыне пункты достижений'),
        ),
    ]
