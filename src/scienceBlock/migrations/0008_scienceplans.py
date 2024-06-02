# Generated by Django 5.0.2 on 2024-06-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0007_remove_sciencesovet_addinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SciencePlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок Совета')),
                ('title_ru', models.TextField(null=True, verbose_name='Заголовок Совета')),
                ('title_kk', models.TextField(null=True, verbose_name='Заголовок Совета')),
                ('content', models.TextField(blank=True, verbose_name='Основная информация')),
                ('content_ru', models.TextField(blank=True, null=True, verbose_name='Основная информация')),
                ('content_kk', models.TextField(blank=True, null=True, verbose_name='Основная информация')),
            ],
            options={
                'verbose_name': 'Информация',
                'verbose_name_plural': 'Научные планы',
            },
        ),
    ]
