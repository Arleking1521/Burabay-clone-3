# Generated by Django 5.0.2 on 2024-03-29 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_pages', '0002_contacts_info_kk_contacts_info_ru_contacts_title_kk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='info_kk',
            new_name='info_kz',
        ),
        migrations.RenameField(
            model_name='contacts',
            old_name='title_kk',
            new_name='title_kz',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='name_kk',
            new_name='name_kz',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='post_kk',
            new_name='post_kz',
        ),
        migrations.RenameField(
            model_name='managers',
            old_name='reception_kk',
            new_name='reception_kz',
        ),
    ]