# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_post_content_en_post_title_en_postattachment_file_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_kk',
            new_name='content_kz',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_kk',
            new_name='title_kz',
        ),
        migrations.RenameField(
            model_name='postattachment',
            old_name='file_kk',
            new_name='file_kz',
        ),
        migrations.RenameField(
            model_name='postattachment',
            old_name='post_kk',
            new_name='post_kz',
        ),
        migrations.RenameField(
            model_name='postattachment',
            old_name='type_kk',
            new_name='type_kz',
        ),
    ]
