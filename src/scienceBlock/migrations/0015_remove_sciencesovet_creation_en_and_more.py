# Generated by Django 5.0.2 on 2024-07-25 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0014_remove_sciencesovet_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sciencesovet',
            name='creation_en',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='creation_kk',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='creation_ru',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='regulation_en',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='regulation_kk',
        ),
        migrations.RemoveField(
            model_name='sciencesovet',
            name='regulation_ru',
        ),
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='sovet_en',
        ),
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='sovet_kk',
        ),
        migrations.RemoveField(
            model_name='sciencesovetplans',
            name='sovet_ru',
        ),
    ]
