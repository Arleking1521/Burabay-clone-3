# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history_legends', '0010_alter_history_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='info_en',
            field=models.TextField(null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='history',
            name='title_en',
            field=models.CharField(null=True, verbose_name='Название'),
        ),
    ]
