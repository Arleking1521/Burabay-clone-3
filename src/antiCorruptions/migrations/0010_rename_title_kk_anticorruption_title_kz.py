# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('antiCorruptions', '0009_anticorruption_title_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anticorruption',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]
