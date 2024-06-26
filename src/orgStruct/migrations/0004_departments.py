# Generated by Django 5.0.2 on 2024-05-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgStruct', '0003_alter_orgstruct_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название отдела')),
                ('info', models.TextField(verbose_name='Информация об отделе')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
    ]
