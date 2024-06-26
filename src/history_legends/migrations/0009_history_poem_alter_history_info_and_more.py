# Generated by Django 5.0.2 on 2024-05-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_legends', '0008_alter_history_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='poem',
            field=models.TextField(default=1, verbose_name='Стихотворение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='history',
            name='info',
            field=models.TextField(verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='history',
            name='info_kk',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='history',
            name='info_ru',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='history',
            name='title',
            field=models.CharField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='history',
            name='title_kk',
            field=models.CharField(null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='history',
            name='title_ru',
            field=models.CharField(null=True, verbose_name='Название'),
        ),
    ]
