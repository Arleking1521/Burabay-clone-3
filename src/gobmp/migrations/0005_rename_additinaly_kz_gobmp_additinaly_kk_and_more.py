# Generated by Django 5.0.2 on 2024-06-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobmp', '0004_rename_additinaly_kk_gobmp_additinaly_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gobmp',
            old_name='additinaly_kz',
            new_name='additinaly_kk',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='adult_kz',
            new_name='adult_kk',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='children_kz',
            new_name='children_kk',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='info_kz',
            new_name='info_kk',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='title_kz',
            new_name='title_kk',
        ),
    ]