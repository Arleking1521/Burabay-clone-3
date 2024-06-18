# Generated by Django 5.0.2 on 2024-06-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GOBMP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название')),
                ('title_ru', models.CharField(null=True, verbose_name='Название')),
                ('title_kk', models.CharField(null=True, verbose_name='Название')),
                ('info', models.TextField(verbose_name='Информация')),
                ('info_ru', models.TextField(null=True, verbose_name='Информация')),
                ('info_kk', models.TextField(null=True, verbose_name='Информация')),
            ],
            options={
                'verbose_name': 'Информация о ГОБМП',
                'verbose_name_plural': 'ГОБМП',
            },
        ),
    ]