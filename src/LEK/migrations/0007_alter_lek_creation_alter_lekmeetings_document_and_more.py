# Generated by Django 5.0.2 on 2024-09-26 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEK', '0006_lek_creation_title_en_lek_creation_title_kk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lek',
            name='creation',
            field=models.FileField(blank=True, upload_to='LEK/', verbose_name='Приказ о создании'),
        ),
        migrations.AlterField(
            model_name='lekmeetings',
            name='document',
            field=models.FileField(blank=True, upload_to='LEK/', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='lekplans',
            name='document',
            field=models.FileField(blank=True, upload_to='LEK/', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='lekregulation',
            name='document',
            field=models.FileField(blank=True, upload_to='LEK/', verbose_name='Документ'),
        ),
    ]