# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProvActs', '0010_provacts_description_en'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provacts',
            old_name='description_kk',
            new_name='description_kz',
        ),
    ]