# Generated by Django 5.0.2 on 2024-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_alter_post_options_alter_postattachment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterModelOptions(
            name='postattachment',
            options={'verbose_name': 'Файлы', 'verbose_name_plural': 'Файлы'},
        ),
    ]
