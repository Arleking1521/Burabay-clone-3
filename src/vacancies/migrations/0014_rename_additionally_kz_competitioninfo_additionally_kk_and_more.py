# Generated by Django 5.0.2 on 2024-06-24 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0013_rename_additionally_kk_competitioninfo_additionally_kz_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='additionally_kz',
            new_name='additionally_kk',
        ),
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='addmisions_kz',
            new_name='addmisions_kk',
        ),
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='compAddress_kz',
            new_name='compAddress_kk',
        ),
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='documents_kz',
            new_name='documents_kk',
        ),
        migrations.RenameField(
            model_name='competitioninfo',
            old_name='enterpriseAddress_kz',
            new_name='enterpriseAddress_kk',
        ),
        migrations.RenameField(
            model_name='vacancies',
            old_name='requirement_kz',
            new_name='requirement_kk',
        ),
        migrations.RenameField(
            model_name='vacancies',
            old_name='vacancy_kz',
            new_name='vacancy_kk',
        ),
    ]
