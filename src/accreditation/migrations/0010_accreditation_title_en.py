# Generated by Django 5.0.2 on 2024-06-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0009_accreditation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditation',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Заголовок'),
        ),
    ]