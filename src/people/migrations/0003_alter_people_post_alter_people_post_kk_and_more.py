# Generated by Django 5.0.2 on 2024-04-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_people_post_kk_people_post_ru_alter_people_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='post',
            field=models.CharField(max_length=128, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='people',
            name='post_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='people',
            name='post_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Должность'),
        ),
    ]
