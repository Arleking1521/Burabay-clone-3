# Generated by Django 5.0.2 on 2024-04-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategicDevelopment', '0002_strategicdev_name_kk_strategicdev_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategicdev',
            name='type',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
