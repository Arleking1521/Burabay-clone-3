# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workersInfo', '0008_alter_workersinfo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='workersinfo',
            name='post_en',
            field=models.TextField(null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='workersinfo',
            name='sertificates_en',
            field=models.TextField(null=True, verbose_name='Сертификат специалиста'),
        ),
    ]
