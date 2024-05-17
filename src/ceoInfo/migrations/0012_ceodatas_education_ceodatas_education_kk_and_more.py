# Generated by Django 5.0.2 on 2024-05-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceoInfo', '0011_remove_ceodatas_work_ex_remove_ceodatas_work_ex_kk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceodatas',
            name='education',
            field=models.TextField(default=18, verbose_name='Образование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ceodatas',
            name='education_kk',
            field=models.TextField(null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='ceodatas',
            name='education_ru',
            field=models.TextField(null=True, verbose_name='Образование'),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
    ]
