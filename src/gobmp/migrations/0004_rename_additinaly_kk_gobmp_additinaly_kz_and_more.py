# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gobmp', '0003_gobmp_additinaly_en_gobmp_adult_en_gobmp_children_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gobmp',
            old_name='additinaly_kk',
            new_name='additinaly_kz',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='adult_kk',
            new_name='adult_kz',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='children_kk',
            new_name='children_kz',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='info_kk',
            new_name='info_kz',
        ),
        migrations.RenameField(
            model_name='gobmp',
            old_name='title_kk',
            new_name='title_kz',
        ),
    ]
