# Generated by Django 5.0.2 on 2024-05-24 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutPage', '0006_alter_aboutinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutinfo',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Информация о НИИ'},
        ),
    ]
