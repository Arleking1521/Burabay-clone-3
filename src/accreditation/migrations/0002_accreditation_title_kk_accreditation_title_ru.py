# Generated by Django 5.0.2 on 2024-04-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditation',
            name='title_kk',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='accreditation',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
    ]
