# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0009_index_page_bannercontent_en_index_page_ceo_appeal_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index_page',
            old_name='bannerContent_kk',
            new_name='bannerContent_kz',
        ),
        migrations.RenameField(
            model_name='index_page',
            old_name='ceo_appeal_kk',
            new_name='ceo_appeal_kz',
        ),
        migrations.RenameField(
            model_name='openinfo',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]
