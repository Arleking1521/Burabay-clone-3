# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborProtection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laborprotection',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Контент'),
        ),
        migrations.AddField(
            model_name='laborprotection',
            name='title_en',
            field=models.TextField(null=True, verbose_name='Заголовок'),
        ),
    ]
