# Generated by Django 5.0.2 on 2024-09-26 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scienceBlock', '0017_sciencesovetmeetings_sciencesovetregulation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='science',
            options={'verbose_name': 'Информация', 'verbose_name_plural': 'Научные разработки'},
        ),
        migrations.AlterField(
            model_name='scienceachievments',
            name='info',
            field=models.FileField(upload_to='science/', verbose_name='Презентация'),
        ),
        migrations.AlterField(
            model_name='sciencesovet',
            name='creation',
            field=models.FileField(blank=True, upload_to='science/', verbose_name='Приказ о создании'),
        ),
        migrations.AlterField(
            model_name='sciencesovetmeetings',
            name='document',
            field=models.FileField(blank=True, upload_to='science/', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='sciencesovetplans',
            name='document',
            field=models.FileField(blank=True, upload_to='science/', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='sciencesovetregulation',
            name='document',
            field=models.FileField(blank=True, upload_to='science/', verbose_name='Документ'),
        ),
    ]
