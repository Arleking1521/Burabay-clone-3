# Generated by Django 5.0.2 on 2024-06-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_rename_content_kk_doctors_content_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='content_kz',
            new_name='content_kk',
        ),
        migrations.RenameField(
            model_name='doctors',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='post_kz',
            new_name='post_kk',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='content_kz',
            new_name='content_kk',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='title_kz',
            new_name='title_kk',
        ),
    ]
