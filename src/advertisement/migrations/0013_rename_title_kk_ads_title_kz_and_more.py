# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_ads_title_en_files_name_en'),
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
