# Generated by Django 5.0.2 on 2024-03-29 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewSovet', '0004_rename_title_kk_viewsovet_title_kz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewsovet',
            old_name='title_kz',
            new_name='title_kk',
        ),
    ]
