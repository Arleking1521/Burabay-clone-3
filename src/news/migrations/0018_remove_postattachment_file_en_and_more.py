# Generated by Django 5.0.2 on 2024-06-24 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_rename_content_kz_post_content_kk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postattachment',
            name='file_en',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='file_kk',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='file_ru',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='post_en',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='post_kk',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='post_ru',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='type_en',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='type_kk',
        ),
        migrations.RemoveField(
            model_name='postattachment',
            name='type_ru',
        ),
    ]
