# Generated by Django 5.0.2 on 2024-05-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medServices', '0004_alter_medservices_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medservices',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
    ]