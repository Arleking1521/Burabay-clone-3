# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_page', '0013_pacientinfo_info_en_pacientinfo_title_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pacientinfo',
            old_name='info_kk',
            new_name='info_kz',
        ),
        migrations.RenameField(
            model_name='pacientinfo',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]
