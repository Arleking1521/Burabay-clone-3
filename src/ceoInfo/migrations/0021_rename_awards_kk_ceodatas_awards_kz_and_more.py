# Generated by Django 5.0.2 on 2024-06-24 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceoInfo', '0020_ceodatas_awards_en_ceodatas_dateofbirth_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ceodatas',
            old_name='awards_kk',
            new_name='awards_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='dateOfBirth_kk',
            new_name='dateOfBirth_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='education_kk',
            new_name='education_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='name_kk',
            new_name='name_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='positions_kk',
            new_name='positions_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='post_kk',
            new_name='post_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='publications_kk',
            new_name='publications_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='scientific_kk',
            new_name='scientific_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='sertificates_kk',
            new_name='sertificates_kz',
        ),
        migrations.RenameField(
            model_name='ceodatas',
            old_name='work_kk',
            new_name='work_kz',
        ),
    ]