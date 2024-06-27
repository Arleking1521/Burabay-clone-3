# Generated by Django 5.0.2 on 2024-06-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_pages', '0013_rename_info_kz_contacts_info_kk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='reception',
            field=models.TextField(verbose_name='День и время приема'),
        ),
        migrations.AlterField(
            model_name='managers',
            name='reception_en',
            field=models.TextField(null=True, verbose_name='День и время приема'),
        ),
        migrations.AlterField(
            model_name='managers',
            name='reception_kk',
            field=models.TextField(null=True, verbose_name='День и время приема'),
        ),
        migrations.AlterField(
            model_name='managers',
            name='reception_ru',
            field=models.TextField(null=True, verbose_name='День и время приема'),
        ),
    ]