# Generated by Django 5.0.2 on 2024-03-29 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutPage', '0003_rename_about_kk_aboutinfo_about_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutinfo',
            old_name='About_kz',
            new_name='About_kk',
        ),
        migrations.RenameField(
            model_name='aboutinfo',
            old_name='LDO_kz',
            new_name='LDO_kk',
        ),
    ]
