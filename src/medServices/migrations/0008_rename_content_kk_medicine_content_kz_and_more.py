# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medServices', '0007_medicine_content_en_medicine_title_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='content_kk',
            new_name='content_kz',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]
