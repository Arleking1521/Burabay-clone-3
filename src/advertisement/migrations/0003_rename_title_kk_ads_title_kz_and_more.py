# Generated by Django 5.0.2 on 2024-03-29 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_ads_title_kk_ads_title_ru_files_name_kk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='title_kk',
            new_name='title_kz',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='name_kk',
            new_name='name_kz',
        ),
    ]
