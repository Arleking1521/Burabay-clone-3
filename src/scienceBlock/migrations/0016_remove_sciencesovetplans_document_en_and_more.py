# Generated by Django 5.0.2 on 2024-07-25 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0015_remove_sciencesovet_creation_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='document_en',
        ),
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='document_kk',
        ),
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='document_ru',
        ),
    ]
