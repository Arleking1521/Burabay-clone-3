# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobmp', '0002_gobmp_additinaly_gobmp_additinaly_kk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gobmp',
            name='additinaly_en',
            field=models.TextField(blank=True, null=True, verbose_name='Для получения путевки необходимо'),
        ),
        migrations.AddField(
            model_name='gobmp',
            name='adult_en',
            field=models.TextField(blank=True, null=True, verbose_name='Взрослые'),
        ),
        migrations.AddField(
            model_name='gobmp',
            name='children_en',
            field=models.TextField(blank=True, null=True, verbose_name='Дети'),
        ),
        migrations.AddField(
            model_name='gobmp',
            name='info_en',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='gobmp',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Название'),
        ),
    ]