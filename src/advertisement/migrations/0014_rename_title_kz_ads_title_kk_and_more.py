# Generated by Django 5.0.2 on 2024-06-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0013_rename_title_kk_ads_title_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='files',
            old_name='name_kz',
            new_name='name_kk',
        ),
    ]
