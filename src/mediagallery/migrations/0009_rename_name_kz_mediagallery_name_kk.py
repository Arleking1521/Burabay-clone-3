# Generated by Django 5.0.2 on 2024-06-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediagallery', '0008_rename_name_kk_mediagallery_name_kz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediagallery',
            old_name='name_kz',
            new_name='name_kk',
        ),
    ]
